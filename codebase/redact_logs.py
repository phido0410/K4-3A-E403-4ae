"""Sinh ban audit da luoc tu log tho, de dua len repo cong khai.

Log tho (eval/logs/) chua NGUYEN VAN tin nhan that trong prompt -> khong push.
Ban audit (eval/audit/) giu du thu de xac minh ky thuat ma khong lo du lieu:
mo hinh, phien ban prompt, van tat ngu canh, msg_id da dung, va response tho cua model.

    .venv/bin/python codebase/redact_logs.py
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from decide import an_ma_nguoi_gui  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "eval" / "logs"
OUT = ROOT / "eval" / "audit"


def shape(user_prompt: str) -> dict:
    """Van tat ngu canh: dem tin moi phan + liet ke msg_id (ma da an danh, an toan)."""
    try:
        ctx = json.loads(user_prompt[user_prompt.index("{"):])
    except Exception:
        return {}
    out = {}
    for k, v in ctx.items():
        if isinstance(v, list):
            out[k] = len(v)
    return {"so_tin_moi_phan": out,
            "msg_id_trong_ngu_canh": re.findall(r'"msg_id":\s*"(M\d{5})"', user_prompt)}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for run_dir in sorted(RAW.glob("run-*")):
        entries = []
        for f in sorted(run_dir.glob("*.json")):
            d = json.loads(f.read_text(encoding="utf-8"))
            entries.append({
                "msg_id": d["msg_id"],
                "model": d.get("model"),
                "prompt_version": d.get("prompt_version", "v1"),
                "luc_chay": d.get("luc_chay"),
                "system_prompt_sha256": hashlib.sha256(
                    d["prompt"]["system"].encode()).hexdigest()[:16],
                "ngu_canh": shape(d["prompt"]["user"]),
                "response_tho": an_ma_nguoi_gui(d["response_tho"]),
                "token": d.get("token"),
            })
        note = ("Ban da luoc cua eval/logs/%s. Prompt he thong nam trong codebase/decide.py "
                "(doi chieu bang system_prompt_sha256). Prompt nguoi dung khong dua vao day vi "
                "chua nguyen van tin nhan that; chay lai codebase/run_eval.py tren may co data "
                "pack de dung lai day du." % run_dir.name)
        (OUT / f"{run_dir.name}.json").write_text(
            json.dumps({"_ghi_chu": note, "so_case": len(entries), "cases": entries},
                       ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  {run_dir.name}: {len(entries)} case -> eval/audit/{run_dir.name}.json")


if __name__ == "__main__":
    main()
