"""Sinh dữ liệu thật cho bản mock từ data pack — chỉ dùng trên máy.

Chạy:  python codebase/build_local_data.py
Kết quả: codebase/local-data/k4-data.js  (đã nằm trong .gitignore — KHÔNG commit, KHÔNG đăng lên mạng)
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
def find_pack(name="k4_messages.csv"):
    """Dò data pack ở các vị trí hay gặp, hoặc lấy từ biến môi trường K4_DATA_DIR."""
    import os
    root = Path(__file__).resolve().parent.parent
    cands = []
    if os.environ.get("K4_DATA_DIR"):
        cands.append(Path(os.environ["K4_DATA_DIR"]) / name)
    cands += [root / "data" / "discord-pack" / name,
              root / "Turtorial" / "data" / "discord-pack" / name,
              root / "Tutorial" / "data" / "discord-pack" / name]
    for c in cands:
        if c.exists():
            return c
    raise SystemExit(
        "Khong tim thay data pack. Dat K4_DATA_DIR tro toi thu muc discord-pack, vi du:\n"
        "  K4_DATA_DIR=Turtorial/data/discord-pack python " + __file__)
OUT = ROOT / "codebase" / "local-data" / "k4-data.js"

def main():
    with find_pack().open(encoding="utf-8") as f:
        rows = [
            [r["msg_id"], r["guild"], r["channel"], r["author"], r["is_bot"] == "True",
             r["reply_to"], r["created_at_vn"], int(r["n_attachments"] or 0), r["content"]]
            for r in csv.DictReader(f)
        ]
    rows.sort(key=lambda r: r[6])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(rows, ensure_ascii=False, separators=(",", ":"))
    OUT.write_text(
        "// SINH TỰ ĐỘNG từ data/discord-pack/k4_messages.csv — dữ liệu bảo mật, không commit.\n"
        "// Cột: msg_id, guild, channel, author, is_bot, reply_to, created_at_vn, n_attachments, content\n"
        f"window.K4_MESSAGES = {payload};\n",
        encoding="utf-8",
    )
    print(f"Đã ghi {len(rows)} tin vào {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
