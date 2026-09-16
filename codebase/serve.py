"""Server cuc bo de demo AI that — API key KHONG bao gio ra toi trinh duyet.

    .venv/bin/python codebase/serve.py
    -> http://127.0.0.1:8765

Duong dan:
  /                     ban mock, nhan do NGUOI gan (labels.js)
  /?ai=1                ban mock, nhan do AI sinh (local-data/ai-labels.js)
  POST /api/decide      {"msg_id": "M18056"} -> goi LLM that ngay luc do

Trang duoc chen them mot bang nho o goc phai de bam goi AI truc tiep — chen luc phuc vu,
khong sua mot dong nao trong cp2-mock.html.
"""
from __future__ import annotations

import json
import sys
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

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


PANEL = """
<div id="ai-live" style="position:fixed;right:16px;bottom:16px;width:340px;z-index:99999;
  font:13px/1.5 'Noto Sans',system-ui,sans-serif;background:#1E1F22;color:#DBDEE1;
  border:1px solid #3F4147;border-radius:10px;box-shadow:0 12px 40px rgba(0,0,0,.5);overflow:hidden">
  <div style="padding:9px 12px;background:#2B2D31;border-bottom:1px solid #3F4147;
    display:flex;align-items:center;gap:8px">
    <span style="width:7px;height:7px;border-radius:50%;background:#23A55A"></span>
    <b style="font-size:12px">Hoi AI truc tiep</b>
    <span id="ai-model" style="margin-left:auto;font-size:10px;color:#949BA4"></span>
  </div>
  <div style="padding:12px">
    <div style="display:flex;gap:6px">
      <input id="ai-id" value="M18056" spellcheck="false" style="flex:1;min-width:0;background:#383A40;
        border:1px solid #3F4147;color:#DBDEE1;border-radius:6px;padding:6px 9px;font:inherit">
      <button id="ai-go" style="background:#5865F2;color:#fff;border:0;border-radius:6px;
        padding:6px 13px;font:inherit;font-weight:600;cursor:pointer">Hoi</button>
    </div>
    <div id="ai-out" style="margin-top:10px;font-size:12.5px;color:#949BA4">
      Nhap ma tin roi bam Hoi — se goi model that.</div>
  </div>
</div>
<script>
(function(){
  var COLOR={need:"#F23F43",check:"#F0B232",nogrounding:"#949BA4",done:"#23A55A"};
  var TEN={need:"Can tra loi",check:"Can kiem tra",nogrounding:"Khong co can cu",done:"Da duoc tra loi"};
  var out=document.getElementById("ai-out"), btn=document.getElementById("ai-go");
  fetch("/api/info").then(r=>r.json()).then(d=>{
    document.getElementById("ai-model").textContent=d.model+" · "+d.prompt;});
  function ask(){
    var id=document.getElementById("ai-id").value.trim().toUpperCase();
    btn.disabled=true; out.innerHTML="<span style='color:#949BA4'>dang goi model...</span>";
    var t0=Date.now();
    fetch("/api/decide",{method:"POST",headers:{"Content-Type":"application/json"},
      body:JSON.stringify({msg_id:id})})
      .then(r=>r.json()).then(function(d){
        btn.disabled=false;
        if(d.error){out.innerHTML="<span style='color:#F23F43'>"+d.error+"</span>";return;}
        out.innerHTML=
          '<div style="font-size:12px;color:#949BA4;margin-bottom:6px">'+
            (d.cau_hoi||"").replace(/[<>]/g,"")+'</div>'+
          '<div style="display:inline-block;background:'+COLOR[d.status]+'22;color:'+COLOR[d.status]+
            ';border:1px solid '+COLOR[d.status]+'55;border-radius:999px;padding:2px 9px;'+
            'font-size:11px;font-weight:700">'+(TEN[d.status]||d.status)+'</div>'+
          '<div style="margin-top:8px;color:#DBDEE1">'+d.reason+'</div>'+
          '<div style="margin-top:8px;font-size:11px;color:#6D6F78">can cu: '+
            (d.evidence_msg_ids.join(", ")||"khong co")+' · '+d.ms+'ms · '+d.tokens+' token</div>';
      }).catch(function(e){btn.disabled=false;out.innerHTML="<span style='color:#F23F43'>"+e+"</span>";});
  }
  btn.onclick=ask;
  document.getElementById("ai-id").addEventListener("keydown",function(e){if(e.key==="Enter")ask();});
})();
</script>
"""


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(BASE), **kw)

    def log_message(self, fmt, *args):
        if "/api/" in (args[0] if args else ""):
            super().log_message(fmt, *args)

    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/api/info":
            return self._json({"model": MODEL, "prompt": PROMPT_VERSION})
        if path in ("/", "/cp2-mock.html"):
            html = (BASE / "cp2-mock.html").read_text(encoding="utf-8")
            if "ai=1" in self.path:
                html = html.replace('src="labels.js"', 'src="local-data/ai-labels.js"')
            html = html.replace("</body>", PANEL + "</body>")
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
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
