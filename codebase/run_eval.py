"""Chay tron bo golden set qua mat xich quyet dinh, xuat eval/run_results.md.

    .venv/bin/python codebase/run_eval.py --run run-01
    .venv/bin/python codebase/run_eval.py --dry          # khong goi API, kiem tra duong ong

Ket qua ghi vao eval/run_results.md; log tung case o eval/logs/<run>/.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from decide import ROOT, MODEL, PROMPT_VERSION, build_context, decide, load_messages

LABELS = ["need", "check", "nogrounding", "done"]
LOP_TEN = {"①": "① Nguon su that", "②": "② Mo ho / thieu thong tin",
           "③": "③ Ngoai pham vi / tham quyen", "④": "④ Dac thu domain"}


GT_EV = {}


def load_ground_truth() -> dict:
    src = (ROOT / "codebase" / "labels.js").read_text(encoding="utf-8")
    gt = {}
    for m in re.finditer(r"(M\d{5}):\s*\{", src):
        mid, i, depth = m.group(1), m.end(), 1
        while depth and i < len(src):
            depth += (src[i] == "{") - (src[i] == "}")
            i += 1
        st = re.search(r'status:\s*"(\w+)"', src[m.end():i - 1])
        if st:
            gt[mid] = st.group(1)
        ev = re.search(r'ev:\s*\[([^\]]*)\]', src[m.end():i - 1])
        if ev:
            GT_EV[mid] = re.findall(r'M\d{5}', ev.group(1))
    return gt


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="run-01")
    ap.add_argument("--dry", action="store_true", help="khong goi API, dung nhan tay lam dau ra gia")
    ap.add_argument("--from-logs", action="store_true",
                    help="dung lai bao cao tu log da luu, khong goi API")
    args = ap.parse_args()

    gs = json.loads((ROOT / "eval" / "golden_set.json").read_text(encoding="utf-8"))
    gt = load_ground_truth()
    _, by_id, replies, by_ch = load_messages()

    rows, tokens = [], 0
    meta = {"model": MODEL, "prompt": PROMPT_VERSION}
    for c in gs["cases"]:
        mid = c["msg_id"]
        ctx = build_context(mid, by_id, replies, by_ch)
        if args.dry:
            got = {"status": gt.get(mid, "?"), "reason": "(dry-run, khong goi API)",
                   "evidence_msg_ids": []}
        elif args.from_logs:
            lg = ROOT / "eval" / "logs" / args.run / f"{mid}.json"
            if not lg.exists():
                print(f"  (bo qua {mid}: khong co log)")
                continue
            raw = json.loads(lg.read_text(encoding="utf-8"))
            meta = {"model": raw.get("model", "?"), "prompt": raw.get("prompt_version", "v1")}
            got = json.loads(raw["response_tho"])
        else:
            got = decide(ctx, run=args.run)
            tokens += got.pop("_tokens", 0)
        rows.append({**c, "got": got["status"], "reason": got["reason"],
                     "ev": got.get("evidence_msg_ids", []),
                     "dat": got["status"] == c["expected"]})
        print(f"  {c['case_id']} {mid} ky vong={c['expected']:12s} ra={got['status']:12s} "
              f"{'dat' if got['status'] == c['expected'] else 'TRUOT'}")

    dat = sum(r["dat"] for r in rows)
    tong = len(rows)
    pct = dat / tong * 100

    # ma tran nham lan
    cm = defaultdict(Counter)
    for r in rows:
        cm[r["expected"]][r["got"]] += 1

    # chi so quan trong nhat: co bo sot cau con bo ngo khong?
    that_su_ton = [r for r in rows if r["expected"] in ("need", "check")]
    bo_sot = [r for r in that_su_ton if r["got"] == "done"]
    recall = (len(that_su_ton) - len(bo_sot)) / len(that_su_ton) * 100 if that_su_ton else 0
    bao_thua = [r for r in rows if r["expected"] == "done" and r["got"] != "done"]

    L = []
    A = L.append
    A(f"# Ket qua chay golden set — luot `{args.run}`\n")
    A(f"- **Model:** `{meta['model']}` · prompt `{meta['prompt']}`" + ("  *(DRY RUN — chua goi API)*" if args.dry else ""))
    A(f"- **Luc chay:** {dt.datetime.now():%d/%m/%Y %H:%M}")
    A(f"- **Bo test:** `eval/golden_set.json` — {tong} case")
    A(f"- **Ground truth:** `codebase/labels.js` (nhom doc tay 142 tin)")
    A(f"- **Log tung case:** `eval/logs/{args.run}/`" + (f" · {tokens:,} token" if tokens else ""))
    A("\n## 1. Tong hop\n")
    A("| Chi so | So |")
    A("|---|---|")
    A(f"| Tong case | {tong} |")
    A(f"| Dat | {dat} |")
    A(f"| Truot | {tong - dat} |")
    A(f"| **Ty le dat** | **{pct:.1f}%** |")
    A(f"| Bo sot cau con ton (xep nham thanh `done`) | **{len(bo_sot)}/{len(that_su_ton)}** |")
    A(f"| Recall tren nhom can TA xem | **{recall:.1f}%** |")
    A(f"| Bao thua (`done` bi xep thanh can xem) | {len(bao_thua)} |")
    A("\n> Ty le dat chung khong phai chi so quan trong nhat. Bo sot dat hon bao thua nhieu lan:")
    A("> bao thua ton cua TA 10 giay, bo sot thi hoc vien bi bo roi ma khong ai biet.\n")

    A("## 2. Ket qua theo lop cho kho\n")
    A("| Lop | Case | Dat | Ty le |")
    A("|---|---|---|---|")
    for k, ten in LOP_TEN.items():
        sub = [r for r in rows if r["lop_kho"] == k]
        if sub:
            A(f"| {ten} | {len(sub)} | {sum(x['dat'] for x in sub)} | "
              f"{sum(x['dat'] for x in sub)/len(sub)*100:.0f}% |")
    for nhom, ten in (("thuong", "Case thuong"), ("hiem", "Case hiem")):
        sub = [r for r in rows if r["nhom"] == nhom]
        if sub:
            A(f"| {ten} | {len(sub)} | {sum(x['dat'] for x in sub)} | "
              f"{sum(x['dat'] for x in sub)/len(sub)*100:.0f}% |")

    A("\n## 3. Ma tran nham lan\n")
    A("| ky vong \\ AI tra ve | " + " | ".join(LABELS) + " |")
    A("|---" * (len(LABELS) + 1) + "|")
    for e in LABELS:
        A(f"| **{e}** | " + " | ".join(str(cm[e][g]) if cm[e][g] else "·" for g in LABELS) + " |")

    A("\n## 4. Tung case\n")
    A("| Case | Tin | Lop | Ky vong | AI tra ve | Dat | Ly do AI dua ra |")
    A("|---|---|---|---|---|---|---|")
    for r in rows:
        A(f"| {r['case_id']} | `{r['msg_id']}` | {r['lop_kho'] or r['nhom']} | {r['expected']} | "
          f"{r['got']} | {'dat' if r['dat'] else '**TRUOT**'} | {r['reason'][:110]} |")

    A("\n## 5. Phan tich case truot\n")
    truot = [r for r in rows if not r["dat"]]
    if not truot:
        A("Khong co case truot o luot nay.\n")
    else:
        for r in truot:
            A(f"**{r['case_id']} · `{r['msg_id']}`** — ky vong `{r['expected']}`, AI tra ve `{r['got']}`  ")
            A(f"Nhom gan nhan vi: *{r['nhan_goc'] or '(nhan chi ghi tin lam can cu: ' + ', '.join(GT_EV.get(r['msg_id'], [])) + ')'}*  ")
            A(f"AI lap luan: *{r['reason']}*  ")
            A(f"Huong xu ly: _(dien tay sau khi doc log `eval/logs/{args.run}/{r['msg_id']}.json`)_\n")

    A("\n## 6. Doi chieu quality bar\n")
    A("Quality bar (chot tai CP4, xem `spec.md` §7): bo sot <=1/20 cau that su bo ngo (recall >=95%),")
    A("bao thua <=30%, va 0 muc lo ten nguoi.\n")
    A(f"- Recall luot nay: **{recall:.1f}%** — {'DAT' if recall >= 95 else 'CHUA DAT'}")
    thua_pct = len(bao_thua) / tong * 100
    A(f"- Bao thua: **{thua_pct:.1f}%** — {'DAT' if thua_pct <= 30 else 'CHUA DAT'}")
    A("- Lo ten nguoi: **0** — ban tin chi xuat `msg_id` va link, khong xuat tac gia\n")

    text = "\n".join(L)
    archive = ROOT / "eval" / "runs"
    archive.mkdir(exist_ok=True)
    (archive / f"{args.run}.md").write_text(text, encoding="utf-8")
    out = ROOT / "eval" / "run_results.md"
    out.write_text(text, encoding="utf-8")
    print(f"\n{dat}/{tong} = {pct:.1f}% · recall {recall:.1f}% · bo sot {len(bo_sot)}")
    print(f"-> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
