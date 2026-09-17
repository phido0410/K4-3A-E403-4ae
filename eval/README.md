# eval/ — bộ kiểm thử và các lượt chạy

Quyết định được đo: **với một câu hỏi + ngữ cảnh quanh nó, hệ thống xếp vào `need` / `check` / `nogrounding` / `done`.**

- Bộ test: [`golden_set.json`](golden_set.json) — 25 case, 100% từ data thật
- Ground truth: `codebase/labels.js` — 142 tin nhóm đọc và gán nhãn tay
- Chẩn đoán từng case trượt: [`phan_tich.json`](phan_tich.json)
- Log thô: `logs/<run>/` (không push — chứa nguyên văn tin thật) · bản đã lược: [`audit/`](audit/)
- Báo cáo từng lượt: [`runs/`](runs/) · lượt mới nhất ở [`run_results.md`](run_results.md)

## Tiến trình

| Lượt | Đổi gì | Đạt | Tỷ lệ | Recall | Bỏ sót |
|---|---|---|---|---|---|
| `run-01` | Lượt đầu, prompt v1 | 10/25 | **40%** | 88.2% | 2 |
| `run-02` | Prompt v2 — thêm thứ tự quyết định 3 bước | 10/25 | **40%** | 88.2% | 2 |
| `run-03` | Prompt v3 — sửa ranh giới `need`/`check`, siết `nogrounding` | 11/25 | **44%** | 88.2% | 2 |
| `run-04` | Ngữ cảnh v4 — quét cả 30 phút **trước** câu hỏi, thêm `tra_loi_cho` | 13/25 | **52%** | 88.2% | 2 |
| `run-05` | Ngữ cảnh v5 — reply trực tiếp kèm **độ trễ** (trước đó thiếu nên không áp được ngưỡng 2 giờ) | 14/25 | **56%** | 88.2% | 2 |

## Nhãn AI trả về so với kỳ vọng

| Lượt | need | check | nogrounding | done |
|---|---|---|---|---|
| `run-01` | 14 | 5 | 0 | 6 |
| `run-02` | 15 | 2 | 4 | 4 |
| `run-03` | 13 | 5 | 1 | 6 |
| `run-04` | 6 | 12 | 1 | 6 |
| `run-05` | 9 | 10 | 0 | 6 |
| **kỳ vọng** | **10** | **7** | **3** | **5** |

## Từng case qua các lượt

| Case | Tin | Kỳ vọng | run-01 | run-02 | run-03 | run-04 | run-05 |
|---|---|---|---|---|---|---|---|
| GS-01 | `M80884` | nogrounding | need | **nogrounding** | **nogrounding** | **nogrounding** | need |
| GS-02 | `M97637` | nogrounding | done | done | done | done | done |
| GS-03 | `M51326` | nogrounding | done | **nogrounding** | done | done | check |
| GS-04 | `M33885` | need | **need** | **need** | **need** | check | **need** |
| GS-05 | `M00553` | check | need | need | need | **check** | **check** |
| GS-06 | `M54679` | check | need | need | need | **check** | **check** |
| GS-07 | `M30246` | need | **need** | nogrounding | **need** | **need** | **need** |
| GS-08 | `M27566` | need | **need** | **need** | **need** | **need** | **need** |
| GS-09 | `M88027` | check | need | need | need | **check** | **check** |
| GS-10 | `M72484` | need | check | **need** | check | check | check |
| GS-11 | `M18676` | check | need | need | need | **check** | **check** |
| GS-12 | `M67980` | check | **check** | need | **check** | **check** | **check** |
| GS-13 | `M30201` | need | **need** | **need** | **need** | check | check |
| GS-14 | `M36687` | check | need | need | need | need | need |
| GS-15 | `M19124` | check | done | done | done | done | done |
| GS-16 | `M60122` | need | **need** | **need** | **need** | **need** | **need** |
| GS-17 | `M04392` | need | **need** | **need** | **need** | **need** | **need** |
| GS-18 | `M03948` | need | check | **need** | check | check | check |
| GS-19 | `M17206` | need | **need** | nogrounding | **need** | **need** | **need** |
| GS-20 | `M18056` | need | done | done | done | done | done |
| GS-21 | `M83358` | done | **done** | **done** | **done** | **done** | **done** |
| GS-22 | `M15562` | done | check | check | check | check | **done** |
| GS-23 | `M20982` | done | need | need | check | check | check |
| GS-24 | `M49586` | done | **done** | need | need | check | need |
| GS-25 | `M83711` | done | check | check | **done** | **done** | **done** |

*(in đậm = khớp nhãn nhóm)*
