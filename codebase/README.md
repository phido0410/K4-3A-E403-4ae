# codebase/ — Bản mock CP2 · Nhóm 4AE

Lát cắt: **Một TA · cuối ngày muốn biết còn câu nào bỏ ngỏ · AI quyết định mỗi câu hỏi đã thực sự được giải đáp chưa · TA nhận danh sách kèm link tới tin gốc, không nêu tên.**

## ▶ Video đi hết luồng

> **Link:** `https://youtu.be/NdsaCmuDQBQ`
>
> *(Quay màn hình, đi hết một vòng: mở bản tin → 4 trạng thái → bấm sửa một mục → đóng bản tin.)*

**Xem video nếu bạn mở repo này từ GitHub** — bản mock cần dữ liệu thật ở máy mới chạy được (lý do ở mục dưới).

## File trong thư mục

| File | Là gì | Có trong repo? |
|---|---|---|
| `cp2-mock.html` | Bản mock, giao diện mô phỏng Discord | ✅ |
| `labels.js` | **142 tin đã gán nhãn tay**: 21 `need` · 8 `check` · 3 `nogrounding` · 110 `done`. Chỉ `msg_id` + nhãn + lý do nhóm viết | ✅ |
| `build_local_data.py` | Script dựng lại dữ liệu chạy mock, từ data pack trên máy | ✅ |
| `local-data/k4-data.js` | Nguyên văn 1.092 tin nhắn thật | ❌ **Không bao giờ push** |

## Vì sao thiếu một file

`local-data/k4-data.js` chứa **nguyên văn tin nhắn thật của bạn cùng khoá**. Repo nộp bài là repo công khai, nên file đó nằm trong `.gitignore` theo quy định bảo mật dữ liệu của khoá (README gốc, mục "Bảo mật dữ liệu được cung cấp", điều 2 và 3).

Repo chỉ giữ **nhãn** (`msg_id` + phán đoán của nhóm), không giữ nội dung. Nhãn vẫn đủ để kiểm chứng kết quả mà không lộ dữ liệu.

## Chạy mock trên máy

```bash
python -m venv .venv && .venv/bin/pip install -r codebase/requirements.txt
.venv/bin/python codebase/build_local_data.py      # cần data pack
.venv/bin/python codebase/serve.py                 # http://127.0.0.1:8765
```

| Đường dẫn | Nhãn hiển thị do ai quyết định |
|---|---|
| `http://127.0.0.1:8765/` | **người** gán tay (`labels.js`) — bản CP2 |
| `http://127.0.0.1:8765/?ai=1` | **AI** sinh (`local-data/ai-labels.js`) — bản CP3 |

Góc phải màn hình có bảng **Hỏi AI trực tiếp**: nhập mã tin rồi bấm Hỏi, server gọi model thật
và trả kết quả kèm thời gian và số token. **API key nằm ở `.env` phía server, không bao giờ
ra tới trình duyệt.**

## Chạy kiểm thử

```bash
.venv/bin/python codebase/run_eval.py --run run-05     # chạy trọn golden set
.venv/bin/python codebase/run_eval.py --run run-04 --from-logs   # dựng lại báo cáo, không tốn API
.venv/bin/python codebase/export_ai_labels.py --run run-04       # kết quả AI -> nhãn cho mock
```

## Phần nào thật, phần nào mock

| Phần | CP2 |
|---|---|
| Giao diện, phân nhóm 4 trạng thái, panel căn cứ, nút sửa | **thật, bấm được** |
| Dữ liệu tin nhắn | **thật** — 1.092 tin từ data pack |
| **Quyết định "đã được giải đáp chưa"** | **mock** — nhãn người đọc tay trong `labels.js` |

Ở CP3, lời gọi AI thật thay vào đúng ô in đậm, và kết quả được so với chính bộ nhãn này để ra bảng % đầu tiên.

---
Chi tiết thiết kế: [`../spec.md`](../spec.md) §4 và §6.
