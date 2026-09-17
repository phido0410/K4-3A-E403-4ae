"""Server cuc bo de demo AI that — API key KHONG bao gio ra toi trinh duyet.

    .venv/bin/python codebase/serve.py
    -> http://127.0.0.1:8765

Duong dan:
  /                     ban mock
  GET  /api/digest      SSE — chay lenh /question_unanswer: rule loc -> goi LLM song song
  POST /api/decide      {"msg_id": "M18056"} -> goi LLM that cho mot tin
"""
from __future__ import annotations

import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))

from decide import MODEL, PROMPT_VERSION, build_context, decide, load_messages  # noqa: E402

BASE = Path(__file__).resolve().parent
PORT = 8765
_DATA = None


def data():
    global _DATA
    if _DATA is None:
        print("  nap data pack...", flush=True)
        _DATA = load_messages()
    return _DATA


# Rule loc — uu tien KHONG BO SOT. Bat thua thi ton them mot loi goi AI (re);
# bo sot thi cau hoi khong bao gio den tay AI (dat). Xem eval/runs/ luot run-05.
QUESTION = re.compile(
    r"\?"                                                    # co dau hoi
    r"|^\s*(\[@[^\]]+\]\s*)*(cho|ch)\s*(em|mình|e|m|tôi)?\s*(hỏi|xin)"   # "cho minh hoi/xin"
    r"|\b(gì|sao|đâu|nào|mấy|ai|bao giờ|bao lâu|bao nhiêu|khi nào|thế nào"
    r"|làm sao|như thế nào|được không|đc ko|có được|có phải|mấy giờ|sao lại)\b"
    r"|^\s*(cách|quy cách|hướng dẫn|cú pháp|link)\b"          # dang yeu cau: "Cach nop..."
    r"|\b(ai biết|có ai|giúp (mình|em|tôi) với|cho (mình|em|tôi) hỏi)\b"
    r"|\b(hả|hở)\b"                                           # "co diem danh ha mn"
    r"|^\s*(\[@[^\]]+\]\s*)*(hạn nộp|deadline|danh sách|lịch|cú pháp|mã đội|mã nhóm)\b"  # cum danh tu tran
    r"|(nhé|nhỉ|ạ)\s*[.!?]*\s*$",                            # ket cau bang tu hoi/nho va
    re.I)

THANKS = re.compile(
    r"^\W*(dạ|vâng|ok|oke|okey)?\W*(e|em|mình|tôi)?\W*(xin)?\s*(cảm ơn|cám ơn|thanks|tks)", re.I)


def ung_vien(rows, kenh: str, ngay: str) -> list:
    """Buoc 1 — rule loc, KHONG dung AI. Nhung tin co the la cau hoi can nguoi tra loi."""
    out = []
    for r in rows:
        if r["is_bot"] == "True" or r["channel"] != kenh:
            continue
        if not r["created_at_vn"].startswith(ngay):
            continue
        if THANKS.match(r["content"]) or int(r["n_chars"]) < 12:
            continue
        if QUESTION.search(r["content"]):
            out.append(r)
    return out


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(BASE), **kw)

    def log_message(self, fmt, *args):
        # Chi in dong lien quan toi /api/ cho do roi terminal luc quay video.
        # Luu y: log_error truyen HTTPStatus chu khong phai chuoi -> phai ep str().
        if args and "/api/" in str(args[0]):
            super().log_message(fmt, *args)

    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _sse(self, ev: str, obj) -> bool:
        try:
            self.wfile.write(f"event: {ev}\ndata: {json.dumps(obj, ensure_ascii=False)}\n\n".encode())
            self.wfile.flush()
            return True
        except (BrokenPipeError, ConnectionResetError):
            return False

    def digest(self, q):
        kenh = q.get("kenh", ["channel_11"])[0].replace("-", "_")
        ngay = q.get("ngay", ["2026-09-13"])[0]
        if re.fullmatch(r"\d{2}/\d{2}", ngay):
            ngay = f"2026-{ngay[3:]}-{ngay[:2]}"

        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()

        rows, by_id, replies, by_ch = data()
        trong_kenh = [r for r in rows if r["channel"] == kenh and r["created_at_vn"].startswith(ngay)]
        self._sse("quet", {"kenh": kenh, "ngay": ngay, "so_tin": len(trong_kenh)})

        cands = ung_vien(rows, kenh, ngay)
        if not self._sse("ung_vien", {"so_cau": len(cands)}):
            return
        if not cands:
            self._sse("xong", {"items": [], "thong_ke": {}, "loi": "Khong tim thay cau hoi nao trong pham vi nay"})
            return

        t0 = time.time()
        items, tokens, xong = [], 0, 0
        with ThreadPoolExecutor(max_workers=8) as pool:
            fut = {pool.submit(self._mot_cau, m["msg_id"], by_id, replies, by_ch): m["msg_id"]
                   for m in cands}
            for f in as_completed(fut):
                xong += 1
                try:
                    it = f.result()
                except Exception as e:
                    it = {"msg_id": fut[f], "status": "nogrounding",
                          "reason": f"goi model that bai: {e}", "ev": [], "tokens": 0}
                tokens += it.pop("tokens", 0)
                items.append(it)
                if not self._sse("tien_do", {"xong": xong, "tong": len(cands)}):
                    return

        thu_tu = {"need": 0, "check": 1, "nogrounding": 2, "done": 3}
        items.sort(key=lambda x: (thu_tu.get(x["status"], 9), x["msg_id"]))
        tk = {k: sum(1 for i in items if i["status"] == k)
              for k in ("need", "check", "nogrounding", "done")}
        self._sse("xong", {"items": items, "thong_ke": tk, "kenh": kenh, "ngay": ngay,
                           "so_tin": len(trong_kenh), "so_goi": len(cands),
                           "giay": round(time.time() - t0, 1), "tokens": tokens,
                           "model": MODEL, "prompt": PROMPT_VERSION})

    @staticmethod
    def _mot_cau(mid, by_id, replies, by_ch):
        ctx = build_context(mid, by_id, replies, by_ch)
        r = decide(ctx, run="live")
        return {"msg_id": mid, "status": r["status"], "reason": r["reason"],
                "ev": r.get("evidence_msg_ids", []), "tokens": r.get("_tokens", 0)}

    def end_headers(self):
        # Sua code roi tai lai la thay ngay — khong de trinh duyet giu ban cu.
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/api/digest":
            return self.digest(parse_qs(urlparse(self.path).query))
        if path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return
        if path == "/api/info":
            return self._json({"model": MODEL, "prompt": PROMPT_VERSION})
        if path in ("/", "/cp2-mock.html"):
            html = (BASE / "cp2-mock.html").read_text(encoding="utf-8")
            if "ai=1" in self.path:
                html = html.replace('src="labels.js"', 'src="local-data/ai-labels.js"')
            body = html.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            return self.wfile.write(body)
        return super().do_GET()

    def do_POST(self):
        if self.path.split("?")[0] != "/api/decide":
            return self._json({"error": "khong co duong dan nay"}, 404)
        n = int(self.headers.get("Content-Length") or 0)
        try:
            mid = json.loads(self.rfile.read(n) or b"{}").get("msg_id", "").strip()
        except Exception:
            return self._json({"error": "body khong phai JSON"}, 400)

        _, by_id, replies, by_ch = data()
        if mid not in by_id:
            return self._json({"error": f"khong co tin {mid} trong pack"}, 404)

        ctx = build_context(mid, by_id, replies, by_ch)
        t0 = time.time()
        try:
            r = decide(ctx, run="live")
        except Exception as e:
            return self._json({"error": f"goi model that bai: {e}"}, 500)
        return self._json({
            "msg_id": mid,
            "cau_hoi": ctx["cau_hoi"]["noi_dung"][:120],
            "status": r["status"], "reason": r["reason"],
            "evidence_msg_ids": r.get("evidence_msg_ids", []),
            "ms": int((time.time() - t0) * 1000), "tokens": r.get("_tokens", 0),
            "model": MODEL, "prompt": PROMPT_VERSION,
        })


if __name__ == "__main__":
    print(f"  model = {MODEL} · prompt = {PROMPT_VERSION}")
    print(f"  nhan NGUOI gan : http://127.0.0.1:{PORT}/")
    print(f"  nhan AI sinh   : http://127.0.0.1:{PORT}/?ai=1")
    print("  Ctrl+C de dung")
    try:
        ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
    except OSError as e:
        if e.errno != 48:
            raise
        print(f"\n  Cong {PORT} dang co tien trinh khac giu. Tat no roi chay lai:")
        print(f"    pkill -f codebase/serve.py")
        print(f"    lsof -ti:{PORT} | xargs kill -9")
        raise SystemExit(1)
