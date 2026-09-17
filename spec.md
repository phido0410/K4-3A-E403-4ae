# AI SPEC — Còn Bỏ Ngỏ · Nhóm 4AE · Cụm ___
Hướng: **B — Trợ lý Discord** · đề **B2** (tính năng mới cho TA)
Loại: [ ] Tối ưu tính năng có sẵn  [x] Tính năng mới *(cải tiến từ bản tin bot đang chạy)*

> Trạng thái: **§4 và §6 chốt tại CP2 (16/9).** §1–§3, §5, §7–§9 hoàn thiện đến hạn chốt spec 21:00 17/9 (CP4).

---

## §1. User & Job
- **Job executor:** TA / Lab coach trực kênh Discord của khoá, cuối ngày.
- **Core JTBD:** *Khi hết một ngày trực, tôi muốn biết câu hỏi nào của học viên còn bỏ ngỏ, để trả lời hết trước khi học viên bỏ cuộc hoặc hỏi lại.*
- **Problem statement (không chữ AI):** TA phải tự cuộn lại nhiều kênh để tìm câu hỏi chưa ai trả lời; câu trôi thì không ai biết là đã trôi.
- **Evidence (chuẩn B — mining):**
  - **27/66 câu hỏi** học viên hỏi nhau (không tag bot) **không có tin nào reply**, trong 3 ngày 12–14/09/2026 → ≈9 câu/ngày.
  - *Quy tắc đếm (kiểm lại được):* tin `is_bot=False`, `mentions_bot=False`, `n_chars>=12`, có `?` hoặc mở đầu "cho… hỏi", loại tin cảm ơn; "không được trả lời" = không tin nào có `reply_to` trỏ vào nó.
  - *Giới hạn đã biết:* 21/27 câu có tin khác cùng kênh trong 30 phút → đang gán nhãn tay để tách trả lời thật khỏi tin trùng thời điểm. Chỉ 5/508 reply trỏ ra ngoài pack (1,0%), nên rò qua chuỗi reply không phải rủi ro chính.
  - *(cần bổ sung trước CP4)* ≥5 ví dụ nguyên văn dẫn `msg_id` + khảo sát/phỏng vấn TA.

## §2. Impact & quyết định chọn
*(hoàn thiện trước CP4 — bảng ≥3 ứng viên + ứng viên đã loại, theo guide §1.4)*

## §3. Giải pháp tương tự đã nghiên cứu
*(hoàn thiện trước CP4)*

---

## §4. Thiết kế  ← **chốt tại CP2**

### Lát cắt MỘT CÂU
> **Một TA · cuối ngày muốn biết còn câu nào bỏ ngỏ · AI quyết định mỗi câu hỏi trong ngày đã thực sự được giải đáp chưa · TA nhận danh sách câu còn bỏ ngỏ kèm link tới tin gốc, không nêu tên, bấm vào là trả lời đúng chỗ.**

**Vì sao đây là quyết định AI, không phải truy vấn CSDL.** "Không có reply" ≠ "chưa được trả lời", và cả hai chiều đều sai được:
- Có reply nhưng **không phải câu trả lời** — reply là *"em ké câu hỏi ạ"*.
- Không reply nhưng **đã được trả lời** bằng tin thường ngay sau đó (21/27 câu có tin khả nghi trong 30 phút).

### Non-goals (KHÔNG build)
1. **Không tự trả lời học viên.** Bản tin chỉ liệt kê cho TA; mọi câu trả lời do TA gõ.
2. **Không tự nhắn cho học viên** — không DM, không ping, không auto-reply.
3. **Không chấm chất lượng câu trả lời** của TA hay của bot.
4. **Không xếp hạng/định danh học viên** (ai hỏi nhiều, ai chưa được trả lời).
5. Không làm bản tin đa ngôn ngữ, không làm app di động.

### Mức prototype
**Mock** — flow bấm hết được, **chạy trên 1.092 tin thật** của data pack tại máy cá nhân.

| Phần | CP2 (đang có) | CP3 (sẽ làm) |
|---|---|---|
| Giao diện Discord, phân nhóm 4 trạng thái, panel căn cứ, nút sửa | **thật, chạy được** | giữ nguyên |
| Dữ liệu tin nhắn | **thật** — `local-data/k4-data.js` sinh từ `k4_messages.csv` | giữ nguyên |
| **Quyết định "đã được giải đáp chưa"** | **mock — nhãn người đọc tay** trong `codebase/labels.js` | **lời gọi AI thật**, so kết quả với chính bộ nhãn này |
| Link tới tin gốc | cuộn tới tin trong mock | link Discord thật |

**Ranh giới data:** `local-data/k4-data.js` chứa nguyên văn tin nhắn thật → **nằm trong `.gitignore`, không bao giờ push**. Repo chỉ chứa `cp2-mock.html` + `labels.js` (chỉ `msg_id` + nhãn + lý do do nhóm viết, **không có nội dung tin**) + `build_local_data.py` để dựng lại data trên máy.

### Automation: **augment**
AI lập danh sách, **TA quyết định**. Cost-of-error lệch hẳn một bên:
- **Báo thừa** một câu đã được trả lời → TA mất ~10 giây bỏ qua. Rẻ, TA tự thấy ngay.
- **Bỏ sót** một câu thật sự bỏ ngỏ → học viên bị lờ, không ai biết để sửa. Đắt, và không tự lộ ra.

→ Thiết kế ưu tiên **không bỏ sót**, chấp nhận báo thừa, và luôn có người duyệt trước khi chạm tới học viên.

### §4b. Nguyên tắc đã áp dụng
| Nguyên tắc | Áp cụ thể vào đâu trong prototype |
|---|---|
| **G1** · Làm rõ hệ thống làm được gì | Dòng mô tả đầu bản tin: nói rõ chỉ liệt kê câu tồn cho TA, **không tự nhắn cho học viên** |
| **G2** · Làm rõ nó làm tốt đến đâu | Bản tin khai trước phạm vi quét (kênh công khai, 3 ngày) và nhận là có thể bỏ sót |
| **G10** · Thu hẹp phạm vi khi nghi ngờ | Ba trạng thái tách riêng: `Cần trả lời` · `Cần kiểm tra` (không chắc) · `Không có căn cứ` — máy không chắc thì nói không chắc, không xếp bừa |
| **G11** · Giải thích vì sao | Mỗi mục kèm lý do cụ thể, ví dụ *"Có reply sau 3 phút nhưng reply nói về nhận role, không trả lời câu hỏi"* |
| **G9** · Sửa dễ dàng | 5 lý do sửa bấm một nút: đã trả lời ở kênh khác · không phải câu hỏi · trùng câu khác · vẫn chưa trả lời · cần BTC xử lý |
| **G17** · Quyền kiểm soát tổng | Bản tin không gửi tin nào cho học viên; TA tự trả lời trong Discord |

*4 trạng thái trong mock (`need` / `check` / `nogrounding` / `done`) ánh xạ thẳng sang 4 đường đi ở §6.*

---

## §5. Kiểu lỗi — 4 lớp chỗ khó
| # | Lớp | Cụ thể hoá cho lát cắt này |
|---|---|---|
| ① | Nguồn sự thật | AI khẳng định "chưa ai trả lời" khi chưa đọc hết ngữ cảnh — đúng lỗi bản tin bot hiện tại đang mắc (7/22 bullet ghi *"Đã có phản hồi, chưa xác nhận đã xử lý"*) |
| ② | Mơ hồ / thiếu thông tin | Tin không rõ có phải câu hỏi không; tin nhắc tới một tin nằm ngoài phạm vi thu thập |
| ③ | Ngoài phạm vi / thẩm quyền | Câu hỏi cá nhân TA không xử lý được ở Discord (*"check giúp em repo này…"*) |
| ④ | Đặc thù domain | **Lộ danh tính** — bản tin nêu ai hỏi gì; và **sai deadline** nếu bản tin tóm tắt lại nội dung thay vì dẫn link |

*(≥8 kịch bản chi tiết — bổ sung trước CP4)*

## §6. Bốn đường đi của trải nghiệm  ← **chốt tại CP2**
| Đường đi | Hành vi trong prototype |
|---|---|
| **Happy path** | Trạng thái `need` — *Cần trả lời*, mức chắc chắn cao. **21 case** trong bộ nhãn. TA bấm trả lời. |
| **Low-confidence (②)** | Trạng thái `check` — *Cần kiểm tra*. **8 case**, ví dụ *"Có reply sau 3 phút nhưng reply nói về nhận role, không trả lời câu hỏi"*. Máy nói ra chỗ phân vân thay vì xếp bừa. |
| **Failure / không căn cứ (①)** | Trạng thái `nogrounding` — *Không có căn cứ*. **3 case**, tin nhắc tới thứ nằm ngoài phạm vi thu thập. Máy **không đoán**. |
| **Correction (user sửa)** | 5 lý do sửa trên từng mục; mục đổi trạng thái và được ghi lại làm dữ liệu cho lần sau. |
| **Bị đòi ngoài phạm vi (③)** | Nhãn `personal` — việc cá nhân (giấy tờ, điểm danh của tôi): bản tin vẫn liệt kê nhưng **không soạn câu trả lời**, chuyển cho BTC. |
| **Case đặc thù domain (④)** | Bản tin **không hiện tên người hỏi** · **không tự soạn nội dung trả lời** (tránh bịa chính sách deadline) · gửi kênh riêng của TA. |

---

## §7. Kiểm thử
- **Đơn vị một case:** một câu hỏi + ngữ cảnh quanh nó → nhãn `need` / `check` / `nogrounding` / `done`.
- **Golden set:** [`eval/golden_set.json`](eval/golden_set.json) — **25 case**, 3 case mỗi lớp chỗ khó ①②③④, 10 case thường, 4 case hiếm, **100% lấy từ data thật**.
- **Ground truth:** `codebase/labels.js` — 142 tin nhóm đọc và gán nhãn tay.
- **Mô hình:** `gpt-4o-mini` qua OpenAI API, Structured Outputs. Mỗi lần gọi chỉ gửi **một câu hỏi + tối đa 8 tin ngữ cảnh**, không đổ cả pack. Log prompt + response thô của từng case trong `eval/logs/<run>/`.

### Kết quả các lượt chạy

| Lượt | Đổi gì | Đạt | Tỷ lệ | Recall | Bỏ sót |
|---|---|---|---|---|---|
| `run-01` | Lượt đầu, prompt v1 | 10/25 | 40% | 88.2% | 2 |
| `run-02` | Prompt v2 — thêm thứ tự quyết định 3 bước | 10/25 | 40% | 88.2% | 2 |
| `run-03` | Prompt v3 — sửa ranh giới `need`/`check`, siết `nogrounding` | 11/25 | 44% | 88.2% | 2 |
| `run-04` | Ngữ cảnh v4 — quét cả 30 phút trước câu hỏi, thêm `tra_loi_cho` | 13/25 | 52% | 88.2% | 2 |
| `run-05` | Ngữ cảnh v5 — reply trực tiếp kèm độ trễ (trước đó thiếu nên không áp được ngưỡng 2 giờ) | 14/25 | 56% | 88.2% | 2 |

Chi tiết từng lượt và từng case: [`eval/README.md`](eval/README.md) · [`eval/runs/`](eval/runs/)

### Recall của bước lọc — đo riêng

Quyết định AI chỉ nhìn thấy những tin mà **rule lọc** đưa vào. Nếu bước này bỏ sót thì AI không có cơ hội đúng, nên nó phải được đo riêng.

| | Bắt được / tổng |
|---|---|
| `need` | **21/21** |
| `check` | **8/8** |
| `nogrounding` | **3/3** |

Bản đầu chỉ bắt 17/32 — bỏ sót câu hỏi dạng yêu cầu không có dấu hỏi (*"Cách nộp daily stand up"*, *"Hạn nộp Lab02"*), `gì` đứng một mình, và tiểu từ `hả`. Rule đã nới theo hướng **thà bắt thừa còn hơn bỏ sót**: bắt thừa tốn thêm một lời gọi AI (rẻ), bỏ sót thì câu hỏi không bao giờ đến tay AI (đắt).

### Ba nguyên nhân đã truy được

1. **`nogrounding` không được dùng (run-01: 0/25 lần).** Model lập luận đúng rồi gán sai nhãn — `M80884` viết *"không thể kết luận…"* nhưng xuất `need`. Sửa bằng thứ tự quyết định trong prompt → run-02 dùng nhãn này 4 lần.
2. **Ranh giới `need`/`check` trong prompt khác với trong `labels.js`.** Nhóm coi *"có người đụng vào nhưng chưa xong"* (lời hẹn, trỏ sang ticket, né câu hỏi) là `check`; prompt v2 xếp hết vào `need`. Sửa ở v3.
3. **Cửa sổ ngữ cảnh chỉ nhìn tới trước.** `M18676` có câu trả lời mâu thuẫn ở `M19404`, **4 phút trước** câu hỏi — chưa bao giờ được gửi cho model. Sửa ở v4 (quét hai chiều) → +2 case.

### Quality bar — **chốt tại CP4, giữ nguyên sau đó**

> Đạt khi **bỏ sót ≤1/20 câu thật sự còn bỏ ngỏ (recall ≥95%)**, **báo thừa ≤30%**, và **0 mục lộ tên người**.

Đối chiếu `run-04`: recall **88,2% — chưa đạt** (bỏ sót 2) · báo thừa **12% — đạt** · lộ tên **0 — đạt**.

### Còn phải làm trước CP4
- Hai người gán nhãn độc lập trên cùng 20 case để đo độ lệch (guide §2.6 bước 4).
- Xử lý case `M36687`: câu trả lời đến sau **705 phút** qua câu hỏi "ké" của người khác — nằm ngoài mọi cửa sổ thời gian hợp lý. Đây là **giới hạn thiết kế**, cần tìm kiếm theo ngữ nghĩa thay vì theo thời gian.

## §8. Phân công & kế hoạch
*(điền tên — bắt buộc cho R7)* spec · evidence/mining · prompt + AI call · flow/UI · golden set + eval · demo

## §9. Changelog
| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
| 16/9 CP2 | Chốt §4 + §6; dựng bản mock chạy trên data thật tại máy | Phát hiện "không có reply ≠ chưa được trả lời" khi mining → tách 4 trạng thái thay vì một danh sách phẳng |
| 16/9 CP2 | Tách `local-data/` ra khỏi repo, chỉ commit `labels.js` (msg_id + nhãn) | Repo nộp bài là repo công khai; nguyên văn tin nhắn của bạn cùng khoá không được lên mạng |
| 16/9 CP2 | Bỏ phương án bot soạn sẵn câu trả lời cho TA | Bản thử đầu điền sẵn câu như *"BTC có hỗ trợ nới deadline"* — không có nguồn nào trong data nói vậy; Track B yêu cầu deadline chỉ lấy từ nguồn chính thức |
