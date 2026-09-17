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
    pt_file = ROOT / "eval" / "phan_tich.json"
    pt = json.loads(pt_file.read_text(encoding="utf-8")) if pt_file.exists() else {}
    chan_doan, nhom_nn = pt.get("theo_case", {}), pt.get("nhom_nguyen_nhan", {})
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

    # Chi so quan trong nhat: co bo sot cau can TA xem khong?
    # Mau so = MOI case khong phai "done" (need + check + nogrounding = 20),
    # dung theo cach bar viet "bo sot <=1/20". Truoc day chi lay need+check (17)
    # nen recall bi bao cao hon thuc te 3,2 diem. Xem §9 Changelog 17/9.
    khong_done = [r for r in rows if r["expected"] != "done"]
    bo_sot = [r for r in khong_done if r["got"] == "done"]
    recall = (len(khong_done) - len(bo_sot)) / len(khong_done) * 100 if khong_done else 0

    # Bao thua = ty le muc SAI trong so muc that su xuat hien tren ban tin gui TA,
    # khong phai tren tong so case. TA chi nhin thay nhung muc AI xep khac "done".
    trong_ban_tin = [r for r in rows if r["got"] != "done"]
    bao_thua = [r for r in trong_ban_tin if r["expected"] == "done"]
    thua_pct = len(bao_thua) / len(trong_ban_tin) * 100 if trong_ban_tin else 0

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
    A(f"| Bo sot (case khong phai `done` ma AI xep `done`) | **{len(bo_sot)}/{len(khong_done)}** |")
    A(f"| Recall tren {len(khong_done)} case can TA xem | **{recall:.1f}%** |")
    A(f"| Muc xuat hien tren ban tin | {len(trong_ban_tin)} |")
    A(f"| Bao thua (`done` bi dua vao ban tin) | **{len(bao_thua)}/{len(trong_ban_tin)} = {thua_pct:.1f}%** |")
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

    if bo_sot:
        A("\n### Case bi bo sot — loai loi dat nhat\n")
        A("| Case | Tin | Ky vong | AI tra ve |")
        A("|---|---|---|---|")
        for r in bo_sot:
            A(f"| {r['case_id']} | `{r['msg_id']}` | {r['expected']} | done |")
        A("")

    A("\n## 5. Phan tich case truot\n")
    truot = [r for r in rows if not r["dat"]]
    if not truot:
        A("Khong co case truot o luot nay.\n")
    else:
        for r in truot:
            cd = chan_doan.get(r["case_id"], {})
            nn = cd.get("nhom", "?")
            A(f"**{r['case_id']} · `{r['msg_id']}`** — ky vong `{r['expected']}`, AI tra ve `{r['got']}`"
              + (f"  ·  nguyen nhan nhom **{nn}**" if nn != "?" else "") + "  ")
            A(f"Nhom gan nhan vi: *{r['nhan_goc'] or '(nhan chi ghi tin lam can cu: ' + ', '.join(GT_EV.get(r['msg_id'], [])) + ')'}*  ")
            A(f"AI lap luan: *{r['reason']}*  ")
            if cd:
                A(f"**Chan doan:** {cd['chan_doan']}  ")
                A(f"**Huong xu ly:** {cd['huong_xu_ly']}  ")
            else:
                A(f"_Chua chan doan — doc log `eval/logs/{args.run}/{r['msg_id']}.json` roi bo sung vao eval/phan_tich.json_  ")
            A("")

        if nhom_nn:
            dem = Counter(chan_doan.get(r["case_id"], {}).get("nhom", "?") for r in truot)
            A("### Gom theo nhom nguyen nhan\n")
            A("| Nhom | So case | Mo ta |")
            A("|---|---|---|")
            for k in sorted(nhom_nn):
                if dem.get(k):
                    A(f"| **{k}** | {dem[k]} | {nhom_nn[k]} |")
            A("")

    A("\n## 6. Doi chieu quality bar\n")
    A("Quality bar (chot tai CP4, xem `spec.md` §7): bo sot <=1/20 cau that su bo ngo (recall >=95%),")
    A("bao thua <=30%, va 0 muc lo ten nguoi.\n")
    A(f"- Recall luot nay: **{recall:.1f}%** — {'DAT' if recall >= 95 else 'CHUA DAT'}")
    A(f"- Bao thua: **{thua_pct:.1f}%** ({len(bao_thua)}/{len(trong_ban_tin)} muc tren ban tin) — {'DAT' if thua_pct <= 30 else 'CHUA DAT'}")
    A("- Lo ten nguoi: **0** — ban tin chi xuat `msg_id` va link, khong xuat tac gia\n")

    text = "\n".join(L)
    archive = ROOT / "eval" / "runs"
    archive.mkdir(exist_ok=True)
    (archive / f"{args.run}.md").write_text(text, encoding="utf-8")
    out = ROOT / "eval" / "run_results.md"
    out.write_text(text, encoding="utf-8")
    print(f"\n{dat}/{tong} = {pct:.1f}% · recall {recall:.1f}% ({len(khong_done)-len(bo_sot)}/{len(khong_done)}) · bo sot {len(bo_sot)} · bao thua {thua_pct:.1f}%")
    print(f"-> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
