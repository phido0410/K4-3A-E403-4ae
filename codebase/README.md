# codebase/ — Còn Bỏ Ngỏ · Nhóm 4AE · Track B2

Lát cắt: **Một TA · cuối ngày muốn biết còn câu nào bỏ ngỏ · AI quyết định mỗi câu hỏi đã thực sự được giải đáp chưa · TA nhận danh sách kèm link tới tin gốc, không nêu tên.**

Sản phẩm là một **lệnh gạch chéo cho bot Discord**. TA gõ `/question_unanswer` trong kênh riêng, bot quét kênh công khai, gọi LLM phân loại từng câu hỏi, rồi dựng bản tin ngay trong kênh.

## ▶ Video

| Mốc | Nội dung | Link |
|---|---|---|
| **CP3** | 30 giây — gõ lệnh, AI chạy thật, bản tin hiện ra | `<DÁN LINK CP3 VÀO ĐÂY>` |
| CP2 | Đi hết luồng giao diện (bản trước, nhãn còn do người gán) | https://youtu.be/NdsaCmuDQBQ |

**Mở repo này từ GitHub thì xem video** — bản mock cần data pack ở máy mới chạy được, lý do ở mục *Vì sao thiếu một file*.

## Luồng xử lý

```
/question_unanswer kenh:channel-11 ngay:13/09
   │
   ├─ 1. Rule lọc ứng viên câu hỏi          serve.py · ung_vien()      không dùng AI
   ├─ 2. Dựng ngữ cảnh 4 nguồn              decide.py · build_context()  không dùng AI
   │      tin trước 30' · reply trực tiếp · tin sau 30' · tin của chính người hỏi
   ├─ 3. ★ Gọi LLM, 8 luồng song song ★     decide.py · decide()       ← mắt xích quyết định
   └─ 4. Gom thành bản tin 4 trạng thái     need · check · nogrounding · done
```

LLM chỉ quyết định **một câu một lần**: *"câu này đã thực sự được giải đáp chưa?"* — không đọc cả pack.

## File trong thư mục

| File | Là gì | Trong repo? |
|---|---|---|
| `decide.py` | **Mắt xích quyết định.** Dựng ngữ cảnh, gọi OpenAI với Structured Outputs, ghi log prompt + phản hồi thô vào `eval/logs/<run>/` | ✅ |
| `serve.py` | Server cục bộ. Phục vụ mock, endpoint SSE `/api/digest` chạy lệnh, `/api/decide` cho một tin | ✅ |
| `cp2-mock.html` | Giao diện mô phỏng Discord — kênh, tin nhắn, bản tin, panel căn cứ, nút sửa | ✅ |
| `run_eval.py` | Chạy trọn golden set, so với `labels.js`, xuất `eval/run_results.md` | ✅ |
| `labels.js` | **142 tin gán nhãn tay** — ground truth để chấm AI. **Không nạp vào giao diện** | ✅ |
| `mine_evidence.py` | In lại mọi số liệu trong `evidence/mining-cau-hoi-ton.md` | ✅ |
| `redact_logs.py` | Lược log thô thành `eval/audit/` để đưa lên repo công khai | ✅ |
| `build_local_data.py` | Dựng `local-data/k4-data.js` từ data pack trên máy | ✅ |
| `requirements.txt` | `openai`, `python-dotenv` | ✅ |
| `local-data/k4-data.js` | Nguyên văn 1.092 tin nhắn thật | ❌ **không bao giờ push** |
| `.env` | `OPENAI_API_KEY`, `OPENAI_MODEL` | ❌ **không bao giờ push** |

## Vì sao thiếu một file

`local-data/k4-data.js` chứa **nguyên văn tin nhắn thật của bạn cùng khoá**. Repo nộp bài là repo công khai, nên file đó nằm trong `.gitignore` theo quy định bảo mật dữ liệu của khoá (README gốc, mục *Bảo mật dữ liệu được cung cấp*, điều 2 và 3). `eval/logs/` cũng bị chặn vì phần prompt chứa nguyên văn tin.

Repo giữ **nhãn và bản audit đã lược** — đủ để kiểm chứng kết quả mà không lộ dữ liệu.

## Chạy trên máy

```bash
python3 -m venv .venv
.venv/bin/pip install -r codebase/requirements.txt
echo 'OPENAI_API_KEY=sk-...'  >> .env
echo 'OPENAI_MODEL=gpt-4o-mini' >> .env

.venv/bin/python codebase/build_local_data.py    # cần data pack
.venv/bin/python codebase/serve.py               # http://127.0.0.1:8765
```

Mở trang, vào kênh riêng **#ban-tin-cau-hoi**, gõ `/` rồi **Tab** để hoàn thành lệnh:

```
/question_unanswer kenh:channel-11 ngay:13/09
```

Gợi ý kênh và ngày lấy từ chính data đang nạp. Phạm vi quyết định thời gian chờ:

| Phạm vi | Lời gọi AI | Thời gian |
|---|---|---|
| `channel-11` · 13/09 | 22 | ~6s |
| `channel-02` · 13/09 | 36 | ~8s |
| `channel-10` · 14/09 | 133 | ~50s |

**API key nằm ở `.env` phía server, không bao giờ ra tới trình duyệt.** Server tự tắt bản cũ đang giữ cổng 8765 khi khởi động. Dừng bằng **Ctrl+C**.

## Chạy kiểm thử

```bash
.venv/bin/python codebase/run_eval.py --run run-06              # chạy trọn golden set
.venv/bin/python codebase/run_eval.py --run run-05 --from-logs  # dựng lại báo cáo, không tốn API
.venv/bin/python codebase/redact_logs.py                        # lược log cho repo
.venv/bin/python codebase/mine_evidence.py                      # in lại số liệu evidence
```

Kết quả và phân tích: [`../eval/`](../eval/) · [`../eval/README.md`](../eval/README.md)

## Phần nào thật, phần nào mock — CP3

| Phần | Trạng thái |
|---|---|
| **Quyết định "đã được giải đáp chưa"** | **AI thật** — `gpt-4o-mini`, log đầy đủ trong `eval/logs/` |
| Dữ liệu tin nhắn | **thật** — 1.092 tin từ data pack |
| Rule lọc ứng viên, dựng ngữ cảnh, gom bản tin | **thật** — code trong repo |
| Giao diện Discord | **mock** — dựng lại bằng HTML, không phải bot chạy trong Discord thật |
| Nút "Trả lời tại tin gốc" | **mock** — tin chỉ lưu trong trang, không gửi đi đâu |

Bước tiếp theo để thành sản phẩm thật: thay giao diện mock bằng `discord.py`, giữ nguyên `decide.py`.

---
Thiết kế: [`../spec.md`](../spec.md) §4 và §6 · Kết quả đo: `../spec.md` §7
