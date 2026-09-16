"""Bien ket qua AI thanh file nhan co cung hinh dang voi labels.js.

Nho vay ban mock hien ket qua AI ma KHONG phai sua mot dong nao trong cp2-mock.html:
no van doc window.K4_LABELS nhu cu, chi khac nguon.

    .venv/bin/python codebase/export_ai_labels.py --run run-04
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="run-04")
    args = ap.parse_args()

    src = ROOT / "eval" / "logs" / args.run
    if not src.exists():
        raise SystemExit(f"Khong co log {src}. Chay run_eval.py truoc.")

    labels, model, ver = {}, None, None
    for f in sorted(src.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        r = json.loads(d["response_tho"])
        model, ver = d.get("model"), d.get("prompt_version", "v1")
        labels[d["msg_id"]] = {"status": r["status"], "reason": r["reason"],
                               "ev": r.get("evidence_msg_ids", []), "nguon": "AI"}

    out = ROOT / "codebase" / "local-data" / "ai-labels.js"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        f"// SINH TU eval/logs/{args.run} — nhan do AI sinh, KHONG phai nguoi gan.\n"
        f"// model={model} · prompt={ver} · {len(labels)} case\n"
        f"window.K4_LABELS = {json.dumps(labels, ensure_ascii=False, indent=1)};\n"
        f"window.K4_LABELS_NGUON = {json.dumps({'run': args.run, 'model': model, 'prompt': ver}, ensure_ascii=False)};\n",
        encoding="utf-8")
    print(f"{len(labels)} nhan AI -> codebase/local-data/ai-labels.js  (model={model}, prompt={ver})")


if __name__ == "__main__":
    main()
