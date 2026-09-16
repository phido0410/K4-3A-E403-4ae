"""In lại toàn bộ số liệu trong evidence/mining-cau-hoi-ton.md.

Chạy:  python codebase/mine_evidence.py
Cần:   data/discord-pack/k4_messages.csv (data pack, không nằm trong repo)
"""
import csv
import datetime as dt
import re
from collections import Counter, defaultdict
from pathlib import Path

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

THANKS = re.compile(
    r"^\W*(dạ|vâng|ok|oke|okey)?\W*(e|em|mình|tôi)?\W*(xin)?\s*(cảm ơn|cám ơn|thanks|tks)", re.I)

# (A) cach dem ngay tho ban dau: coi chu "a" la dau hieu cau hoi -> DINH BAY
NAIVE = re.compile(
    r"\?|\b(ạ|nhỉ|không ạ|ko ạ|vậy ạ)\b|^(cho (em|mình|e|m) hỏi)"
    r"|\b(khi nào|bao giờ|ở đâu|thế nào|làm sao|như thế nào|có được|được không"
    r"|đc ko|bao nhiêu|sao để|có phải)\b", re.I)

# (B) quy tac muc 1 cua evidence/mining-cau-hoi-ton.md
RULE1 = re.compile(
    r"\?|^\s*(\[@[^\]]+\]\s*)*(cho|ch)\s*(em|mình|e|m|tôi)?\s*hỏi"
    r"|\b(khi nào|bao giờ|ở đâu|làm sao|như thế nào|thế nào|bao nhiêu|được không"
    r"|đc ko|có được|có phải|mấy giờ|mấy bạn|sao lại|là gì|nào ạ)\b", re.I)

# (C) ban siet: bat buoc co "?" hoac "cho ... hoi"
TIGHT = re.compile(
    r"\?|^\s*(\[@[^\]]+\]\s*)*(cho|ch)\s*(em|mình|e|m|tôi)?\s*hỏi", re.I)

def is_question(row, mode="rule1"):
    """mode: naive (A) | rule1 (B) | tight (C) — xem evidence/mining-cau-hoi-ton.md muc 1-2."""
    if mode == "naive":
        return bool(NAIVE.search(row["content"]))
    if THANKS.match(row["content"]) or int(row["n_chars"]) < 12:
        return False
    return bool((RULE1 if mode == "rule1" else TIGHT).search(row["content"]))


def main():
    rows = list(csv.DictReader(find_pack().open(encoding="utf-8")))
    by_id = {r["msg_id"]: r for r in rows}
    replies = defaultdict(list)
    for r in rows:
        if r["reply_to"]:
            replies[r["reply_to"]].append(r)

    people = [r for r in rows if r["is_bot"] == "False"]
    print(f"Tổng tin                : {len(rows)}")
    print(f"  người / bot           : {len(people)} / {len(rows) - len(people)}")
    print(f"  kênh                  : {Counter(r['channel'] for r in rows).most_common(3)}")

    print("\nMUC 2 — bay dem (bang trong evidence):")
    for mode, ten in (("naive", 'dung chu "a"'), ("rule1", "quy tac muc 1")):
        q = [r for r in people if is_question(r, mode)]
        n = sum(1 for r in q if not replies[r["msg_id"]])
        print(f"  {ten:16s}: {len(q):4d} cau hoi | khong reply {n/len(q)*100:.1f}%")

    # Muc 3
    q_all = [r for r in people if is_question(r, "rule1")]
    to_human = [r for r in q_all if r["mentions_bot"] == "False"]
    tight = [r for r in to_human if is_question(r, "tight")]
    drift = [r for r in tight if not replies[r["msg_id"]]]
    print(f"\nCâu hỏi (quy tắc mục 1) : {len(q_all)}")
    print(f"  hỏi bot               : {len(q_all) - len(to_human)}")
    print(f"  hỏi người             : {len(to_human)}")
    print(f"  siết (bắt buộc ? )    : {len(tight)}")
    print(f"  >>> KHÔNG CÓ REPLY    : {len(drift)}  (~{len(drift)/3:.0f} câu/ngày)")

    # Muc 4: gioi han da do
    near = 0
    by_ch = defaultdict(list)
    for r in rows:
        by_ch[r["channel"]].append(r)
    for ch in by_ch.values():
        ch.sort(key=lambda r: r["created_at_vn"])
    t = lambda s: dt.datetime.strptime(s, "%Y-%m-%d %H:%M")
    for r in drift:
        seq = by_ch[r["channel"]]
        for k in seq[seq.index(r) + 1:]:
            if (t(k["created_at_vn"]) - t(r["created_at_vn"])).total_seconds() > 1800:
                break
            if k["author"] != r["author"] and int(k["n_chars"]) >= 20 \
                    and k["is_bot"] == "False" and not is_question(k, "tight"):
                near += 1
                break
    print(f"\nGIỚI HẠN — trong {len(drift)} câu trôi, {near} câu có tin khác cùng kênh "
          f"trong 30' ({near/len(drift)*100:.0f}%) → có thể đã được trả lời không bấm reply")

    out = [r for r in rows if r["reply_to"] and r["reply_to"] not in by_id]
    tot = sum(1 for r in rows if r["reply_to"])
    print(f"Reply trỏ ra ngoài pack : {len(out)}/{tot} ({len(out)/tot*100:.1f}%)")


if __name__ == "__main__":
    main()
