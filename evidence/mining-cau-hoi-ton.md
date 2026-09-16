# Log mining — câu hỏi còn bỏ ngỏ trên Discord khoá 4

Nguồn: `data/discord-pack/k4_messages.csv` — 1.092 tin, 12–14/09/2026, 202 tác giả, đã ẩn danh.
Mục đích: chứng minh pain *"câu hỏi của học viên trôi mà không ai biết"* bằng số đếm lại được.
**Trích dẫn tối đa 2 câu mỗi ví dụ, dẫn `msg_id`** theo quy định `data/discord-pack/README.md`.

## 1. Quy tắc đếm

Người khác chạy lại phải ra cùng số. Ba bước:

**Bước 1 — lọc tin của người.** `is_bot = False` → **779/1.092 tin** (bot chiếm 313, tức 28,7%).

**Bước 2 — nhận diện câu hỏi.** Một tin được tính là câu hỏi khi thoả **tất cả**:
- `n_chars >= 12`
- có dấu `?` **hoặc** mở đầu bằng *"cho … hỏi"*
- **không** phải tin cảm ơn (khớp `^(dạ|vâng|ok)?\s*(e|em|mình|tôi)?\s*(cảm ơn|cám ơn|thanks|tks)`)

**Bước 3 — tách theo người nhận.** `mentions_bot = True` là hỏi bot; `False` là hỏi người.

## 2. Vì sao phải loại tin cảm ơn — một bẫy đếm thật

Bản đếm đầu dùng chữ **"ạ"** làm dấu hiệu câu hỏi. Hậu quả: *"Dạ e cảm ơn ạ!"* (`M11917`) bị tính là câu hỏi chưa được trả lời.

| Cách đếm | Số câu hỏi | Tỷ lệ không có reply |
|---|---|---|
| Dùng "ạ" làm dấu hiệu | 304 | 26,3% |
| **Quy tắc ở mục 1** | **221** | **17,2%** |

Chênh 83 tin. Số dùng trong spec là số của quy tắc mục 1.

## 3. Kết quả đếm

| Chỉ số | Số |
|---|---|
| Tin của người | 779 |
| Câu hỏi | 221 (28,4% tin người) |
| → hỏi bot (`mentions_bot=True`) | 134 |
| → **hỏi người** | **87** |
| Trong nhóm hỏi người: siết thêm (bắt buộc có `?` hoặc *"cho…hỏi"*) | 66 |
| → **không có tin nào reply** | **27** |

**≈9 câu/ngày trôi** trên 3 kênh chính (`channel_10` 654 tin · `channel_02` 200 · `channel_11` 170 — chiếm 94% lưu lượng).

## 4. Giới hạn đã đo, không giấu

**"Không có reply" chưa chắc là "chưa ai trả lời".** Trong 27 câu, **21 câu (78%)** có một tin khác cùng kênh trong vòng 30 phút, của người khác — có thể là câu trả lời gõ thẳng chứ không bấm nút reply.

Đã kiểm ngược chiều rò rỉ khác: chỉ **5/508 tin reply (1,0%)** trỏ tới tin gốc nằm ngoài pack, nên chuỗi reply trong pack gần như đầy đủ.

Giới hạn của chính pack: 3 ngày, chỉ kênh public, không có tên kênh, Mod/TA và học viên đều là `D####` nên **không phân biệt được ai là TA**, và 8 tin hoàn cảnh cá nhân đã bị BTC loại.

## 5. Gán nhãn tay — và phát hiện quan trọng nhất

Vì quy tắc máy không kết luận được, nhóm **đọc tay 142 tin** và gán nhãn (`codebase/labels.js`):

| Nhãn | Số |
|---|---|
| `need` — còn bỏ ngỏ | 21 |
| `check` — không chắc, cần người xem | 8 |
| `nogrounding` — không đủ căn cứ | 3 |
| `done` — đã được giải đáp | 110 |

**Phát hiện: có reply ≠ đã được trả lời.** 9/142 tin có tin phản hồi nhưng nhãn không phải `done`:

| Mã tin | Chuyện gì xảy ra |
|---|---|
| `M30201` | Có reply sau 3 phút, nhưng reply nói về nhận role |
| `M36687` | Reply là *"em ké câu hỏi ạ"* — hỏi ké, không phải trả lời |
| `M00553` | Chỉ được hẹn *"mai hỏi luôn"* |
| `M54679` | Có phản hồi nhưng né câu hỏi |
| `M18676` | Hai bạn học trả lời **mâu thuẫn nhau** về điểm danh workshop |
| `M67980` | Câu trả lời đến từ bạn học, chưa phải nguồn chính thức |

Và chiều ngược lại — `M99769` *"cho mình hỏi một team mấy bạn?"* không có reply, nhưng tin ngay sau trong kênh đã trả lời đúng ý.

**Đây là lý do bài toán cần AI.** Nếu *"chưa ai trả lời" = "không có reply"* thì một câu truy vấn là xong. Cả hai chiều đều sai được, nên quyết định phải đọc được ngữ cảnh.

## 6. Ví dụ nguyên văn *(≤2 câu mỗi ví dụ)*

| Mã tin | Trích | Vì sao đáng chú ý |
|---|---|---|
| `M99769` | *"cho mình hỏi một team mấy bạn?"* | Không reply nhưng đã được trả lời ngay sau |
| `M36687` | reply: *"em ké câu hỏi ạ"* | Có reply nhưng không phải trả lời |
| `M49586` | *"Kiểu em ko có câu hỏi nào hỏi, có ổn ko ạ :))"* | Ranh giới: có phải câu hỏi cần trả lời không? |
| `M18746` | *"check giúp em repo này đã đủ 5 thành viên chưa với ạ"* | Việc cá nhân — ngoài thẩm quyền trả lời tự động |
| `M51326` | Nội dung lỗi nằm trong 2 ảnh đính kèm | Hệ thống không đọc ảnh → không đủ căn cứ |

## 7. Cách chạy lại

```bash
python codebase/build_local_data.py   # cần data pack ở data/discord-pack/
python codebase/mine_evidence.py      # in lại toàn bộ số ở mục 3
```

Bộ nhãn tay dùng làm ground truth cho golden set: `eval/golden_set.json`.
