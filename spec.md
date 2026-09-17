# AI SPEC — Còn Bỏ Ngỏ · Nhóm 4AE · Cụm ___
Hướng: **B — Trợ lý Discord** · đề **B2** (tính năng mới cho TA)
Loại: [ ] Tối ưu tính năng có sẵn  [x] Tính năng mới *(cải tiến từ bản tin bot đang chạy)*

> **Trạng thái: chốt tại CP4 — 17/9/2026, trước 21:00.** Quality bar ở §7 khoá từ thời điểm này và giữ nguyên đến CP6.
> §4 và §6 chốt tại CP2 (16/9), không sửa. Phần chưa làm xong được tự khai ở cuối §7.

---

## §1. User & Job

- **Job executor:** TA / Lab coach trực kênh Discord của khoá, cuối ngày.
- **Workflow hiện tại:** cuộn lại từng kênh công khai → đọc bản tin ngày do bot tự sinh → tự đoán câu nào chưa ai trả lời → trả lời. Bản tin hiện tại không có link tới từng câu hỏi và không tách được "đã có phản hồi" với "đã giải quyết".
- **Core JTBD:** *Khi hết một ngày trực, tôi muốn biết câu hỏi nào của học viên còn bỏ ngỏ, để trả lời hết trước khi học viên bỏ cuộc hoặc hỏi lại.*
- **Problem statement (không chữ AI):** TA phải tự cuộn lại nhiều kênh để tìm câu hỏi chưa ai trả lời; câu trôi thì không ai biết là đã trôi.

### Evidence — chuẩn B (mining)

Log đầy đủ, quy tắc đếm và cách chạy lại: [`evidence/mining-cau-hoi-ton.md`](evidence/mining-cau-hoi-ton.md) · in lại mọi số: `python codebase/mine_evidence.py`.

| Chỉ số | Số | Quy tắc đếm |
|---|---|---|
| Câu hỏi học viên hỏi người (không tag bot) | **66** | `is_bot=False`, `mentions_bot=False`, `n_chars>=12`, có `?` hoặc mở đầu "cho… hỏi", loại tin cảm ơn |
| → **không có tin nào reply** | **27/66** ≈ **9 câu/ngày** | không tin nào có `reply_to` trỏ vào |
| Nhóm đọc tay 142 tin, gán nhãn | `need` 21 · `check` 8 · `nogrounding` 3 · `done` 110 | [`codebase/labels.js`](codebase/labels.js) |
| **Có reply nhưng chưa được giải đáp** | **9/142** | tin có phản hồi nhưng nhãn tay khác `done` |
| Rò qua chuỗi reply | 5/508 reply (1,0%) trỏ ra ngoài pack | chuỗi reply trong pack gần như đầy đủ |

**Baseline — bản tin ngày bot đang chạy** (`k4_daily_reports.md`, 4 bản tin, đếm chuỗi trực tiếp):

| Lỗi | Số |
|---|---|
| Mục ghi *"Đã có phản hồi, chưa xác nhận đã xử lý"* — không nói được câu nào còn cần TA | **7/22** gạch đầu dòng |
| Gạch đầu dòng gắn tên người (`[HV]`) | **16/22** |
| Bản tin ngày 14/09 có link tới từng câu hỏi | **0/2** |
| Chuỗi "nguồn tham chiếu" chèn vào giữa từ | **14** lần (1 bản tin) |
| Tóm tắt bị cắt cụt giữa câu | **2/4** bản tin |

**Ví dụ nguyên văn** *(≤2 câu mỗi ví dụ, dẫn `msg_id`, không nêu người gửi)*:

| Mã tin | Trích | Vì sao đáng chú ý |
|---|---|---|
| `M99769` | *"cho mình hỏi một team mấy bạn?"* | Không có reply nhưng tin ngay sau trong kênh đã trả lời đúng ý |
| `M36687` | reply đầu tiên: *"em ké câu hỏi ạ"* | Có reply nhưng là hỏi ké, không phải câu trả lời |
| `M30201` | *"…cho em hỏi điểm chuyên cần ở vin uni tính như thế nào ah?"* | Có reply sau 3 phút nhưng reply nói về nhận role |
| `M49586` | *"Kiểu em ko có câu hỏi nào hỏi, có ổn ko ạ :))"* | Ranh giới: có phải câu hỏi cần trả lời không |
| `M18746` | *"check giúp em repo này đã đủ 5 thành viên chưa với ạ"* | Việc cá nhân — ngoài thẩm quyền trả lời tự động |
| `M51326` | nội dung lỗi nằm trong 2 ảnh đính kèm | Hệ thống không đọc ảnh → không đủ căn cứ |

### Evidence — chuẩn A (khảo sát)

**Chưa có.** Form khảo sát học viên + TA đã soạn (`evidence/khao-sat/`) nhưng **chưa thu đủ ≥20 người** tại CP4. Bằng chứng của nhóm hiện dựa hoàn toàn vào chuẩn B.

---

## §2. Impact & quyết định chọn

Ba ứng viên cùng lấy từ data pack Discord khoá 4 (12–14/09).

| Ứng viên | Bao nhiêu người gặp | Tần suất | Mỗi lần tốn gì | Build nổi? | Chọn? |
|---|---|---|---|---|---|
| **① Bản tin câu hỏi còn bỏ ngỏ cho TA** | 27 câu không reply / 3 ngày; trong 142 tin đọc tay có 32 câu cần TA xem | hằng ngày | Học viên chờ mà không ai biết; có câu hỏi lại sau 3,5 giờ vẫn không ai trả lời (`M30246` → `M48859`) | Có — 1 lời gọi LLM mỗi câu | ✅ **chọn** |
| ② Sửa lỗi bản tin ngày đang chạy | 4/4 bản tin; mọi TA đọc bản tin | hằng ngày | 14 lỗi chèn chữ, 2/4 bản tin cụt → TA mất tin cậy vào bản tin | Có | ❌ loại |
| ③ Bot trả lời câu hỏi hành chính có căn cứ | **130/307** tin tag bot có từ khoá hành chính (`deadline|hạn|nộp|điểm danh|xp|ticket|standup|lịch|mấy giờ`) | nhiều lần/ngày | Trả sai deadline → học viên mất điểm | Khó | ❌ loại |

**Vì sao chọn ①:**
- Pain đếm được (≈9 câu/ngày không có reply).
- Có một quyết định AI thật: *"câu này đã thực sự được giải đáp chưa?"*. Luật "có reply = đã trả lời" sai theo cả hai chiều (9/142 có reply nhưng chưa giải đáp; `M99769` không reply nhưng đã được trả lời).
- Có baseline để so: bản tin bot hiện tại không chỉ ra câu nào còn tồn (7/22 mục "chưa xác nhận đã xử lý").

**Vì sao loại ②:** sửa xong chỉ là bug fix chuỗi ký tự, không có quyết định AI nào. Phần "không nêu tên, có link từng câu" đã gộp vào ①.
**Vì sao loại ③:** không có nguồn chính thức về deadline trong pack để đối chiếu. Làm ra sẽ phải để model tự nói deadline — đúng lỗi Track B cảnh báo.

---

## §3. Giải pháp tương tự đã nghiên cứu

> Viết từ trải nghiệm dùng Discord hằng ngày của nhóm và tài liệu công khai của Zendesk; nhóm chưa dùng thử Zendesk trên tài khoản thật.

**Zendesk — hàng đợi ticket theo trạng thái**
- ① *Flow:* mỗi yêu cầu là một ticket có trạng thái (New → Open → Pending → Solved). Nhân viên hỗ trợ làm việc từ các view lọc sẵn như "ticket chưa giải quyết", "chưa được giao".
- ② *Đáng học:* tách **đã có người trả lời** khỏi **đã giải quyết xong** — Pending nghĩa là đã phản hồi nhưng chưa xong. Đúng ranh giới `check` / `done` của nhóm.
- ③ *Đáng né:* trạng thái do **người đổi tay**. Học viên trên Discord không mở ticket, và không ai đổi trạng thái cho một tin chat.
- ④ *Mình khác:* không bắt ai đổi trạng thái — AI **đọc hội thoại để suy ra trạng thái**, TA chỉ sửa khi AI sai.

**Discord / Slack — tin chưa đọc và "Mark unread"**
- ① *Flow:* ứng dụng đánh dấu kênh có tin chưa đọc; người dùng tự đánh dấu lại một tin là "chưa đọc" để nhớ quay lại.
- ② *Đáng học:* để người dùng **tự đánh dấu lại** bằng một thao tác, không cần giải thích — nhóm áp vào nút "Sửa kết luận".
- ③ *Đáng né:* chỉ biết **đã đọc hay chưa**, không biết **câu hỏi đã được đáp hay chưa**. TA đọc hết mà vẫn không biết câu nào còn trôi.
- ④ *Mình khác:* đơn vị là **câu hỏi**, không phải tin nhắn; trạng thái là **đã giải đáp chưa**, không phải đã đọc chưa.

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

## §5. Kiểu lỗi — 4 lớp chỗ khó + kịch bản

### Bốn lớp, cụ thể hoá cho lát cắt

| # | Lớp | Cụ thể hoá cho lát cắt này |
|---|---|---|
| ① | Nguồn sự thật | AI kết luận "đã giải đáp" hoặc "chưa ai trả lời" khi căn cứ nằm ngoài tầm nhìn (tin nhắn riêng, ảnh, hội thoại khác) — đúng lỗi bản tin bot hiện tại mắc (7/22 mục *"Đã có phản hồi, chưa xác nhận đã xử lý"*) |
| ② | Mơ hồ / thiếu thông tin | Tin không rõ có phải câu hỏi không; phản hồi chỉ là lời hẹn hoặc né câu hỏi |
| ③ | Ngoài phạm vi / thẩm quyền | Việc cá nhân TA không tự quyết ở Discord: giấy tờ, gia hạn, kiểm tra hộ bài nộp |
| ④ | Đặc thù domain | Sai deadline, bạn học trả lời mâu thuẫn, lộ danh tính người hỏi trong bản tin |

### Kịch bản rủi ro

Cột cuối là kết quả AI thật trên golden set, lượt `run-05` ([`eval/runs/run-05.md`](eval/runs/run-05.md)).

| # | Tình huống cụ thể | Lớp | Hành vi mong muốn (nói gì · hiện gì · cho TA làm gì) | Nguyên tắc | Golden set · run-05 |
|---|---|---|---|---|---|
| K1 | Học viên nhờ admin trả lời **tin nhắn riêng** (`M80884`) | ① | `nogrounding`: *"Căn cứ nằm ở tin nhắn riêng, hệ thống không đọc được"* · nút "Mở tin gốc để tự xem" | G10, PAIR Errors | GS-01 · ❌ AI xếp `need` |
| K2 | Nội dung lỗi nằm trong **ảnh đính kèm** (`M51326`) | ① | `nogrounding`: *"Không đọc được ảnh"* · không đoán | G2, G10 | GS-03 · ❌ AI xếp `check` |
| K3 | Câu hỏi nhắc tới **file/link từ hội thoại ngoài phạm vi quét** (`M97637`) | ① | `nogrounding`; **không** được xếp `done` chỉ vì có bot trả lời gần đó | G10 | GS-02 · ❌ AI xếp `done` — **bỏ sót ở cả 5 lượt** |
| K4 | Phản hồi duy nhất là **lời hẹn** "mai hỏi luôn" (`M00553`) | ② | `check`: lời hẹn chưa phải câu trả lời | G11 | GS-05 · ✅ |
| K5 | Có phản hồi nhưng **né câu hỏi** (`M54679`) | ② | `check`, lý do nêu rõ phản hồi không trả lời | G11 | GS-06 · ✅ |
| K6 | Tin **không phải câu hỏi cần trả lời** (`M49586`) | ② | `done` kèm lý do *"không phải câu hỏi cần người trả lời"* — không đẩy vào danh sách TA | G10 | GS-24 · ❌ AI xếp `need` (báo thừa) |
| K7 | Xin **gia hạn nộp lab**, chỉ được trỏ sang ticket (`M88027`) | ③ | `check` · khung "Việc cá nhân": AI **không soạn câu trả lời**, TA/BTC quyết định | G17 | GS-09 · ✅ |
| K8 | Hỏi **giấy tờ cá nhân**, không ai phản hồi (`M27566`, `M30246`) | ③ | `need` · đánh dấu việc cá nhân, chuyển BTC | G17 | GS-07, GS-08 · ✅ |
| K9 | **Hai bạn học trả lời mâu thuẫn** nhau về điểm danh (`M18676`) | ④ | `check`, dẫn cả hai tin làm căn cứ | G11 | GS-11 · ✅ |
| K10 | Hỏi **hạn nộp** trong kênh bot đông tin, không tag bot (`M72484`) | ④ | `need` · bản tin **chỉ dẫn link**, không tóm tắt nội dung deadline | Track B an toàn | GS-10 · ❌ AI xếp `check` |
| K11 | Có trả lời nhưng **sau 8 giờ** (`M19124`) | ④ | `check` — trả lời muộn chưa tính là xong | G11 | GS-15 · ❌ AI xếp `done` — **bỏ sót ở cả 5 lượt** |
| K12 | **Đáp án có sẵn** cho câu y hệt 19 phút trước, nhưng không ai trỏ cho người hỏi (`M18056`) | ② | `need` (quy ước chốt tại CP4 — xem §7) | G10 | GS-20 · ❌ AI xếp `done` — **bỏ sót ở cả 5 lượt** |
| K13 | **Lộ danh tính**: bản tin nêu ai hỏi gì | ④ | Bản tin chỉ xuất `msg_id` + link, không tên, không mã người gửi | — | Kiểm bằng đầu ra bản tin; không có case trong golden set |
| K14 | Tin chứa **chỉ thị** kiểu "bỏ qua hướng dẫn trước đó" | ① | Coi là dữ liệu, phân loại bình thường (đã ghi trong system prompt `decide.py`) | — | **Chưa có case** — pack không có tin nào khớp mẫu này |

**Kịch bản nhóm sợ nhất khi demo: K3, K11, K12.** AI xếp `done` → câu hỏi biến khỏi danh sách TA mà không ai thấy. Cả ba bị xếp sai ở **cả 5 lượt**, chưa lượt sửa prompt nào chạm tới.

---

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

### Hệ thống đang được đo (trạng thái tại CP4)

- **Đơn vị một case:** một câu hỏi + ngữ cảnh quanh nó → một nhãn `need` / `check` / `nogrounding` / `done`.
- **Mô hình:** `gpt-4o-mini`, temperature 0, Structured Outputs, prompt `v5` ([`codebase/decide.py`](codebase/decide.py)).
- **Ngữ cảnh mỗi lời gọi:** tin trong 30 phút trước · reply trực tiếp kèm độ trễ (phút) · tin cùng kênh trong 30 phút sau (tối đa 8 tin mỗi phần) · tin sau đó của chính người hỏi · cờ ảnh đính kèm. Không đổ cả pack.
- **Log:** prompt + phản hồi thô từng case ở `eval/logs/<run>/` (không push — chứa nguyên văn tin); bản đã lược ở [`eval/audit/`](eval/audit/).

### Định nghĩa nhãn — chốt tại CP4

| Nhãn | Định nghĩa |
|---|---|
| `nogrounding` | **Chính câu hỏi** trỏ tới thứ nằm ngoài tầm quan sát: tin nhắn riêng, ảnh đính kèm, file/link/hội thoại không có trong ngữ cảnh, kênh khác. Xét **trước** mọi nhãn khác, kể cả khi có tin trả lời gần đó. |
| `need` | Không ai **nhắm vào** câu hỏi. Tin lạc đề, "+1", "em ké câu hỏi", tin của **chính người hỏi**, và tin trả lời **một câu hỏi khác** đều không tính. |
| `check` | Có người nhắm vào câu hỏi nhưng chưa xong: đến sau **>120 phút** · từ học viên khác, chưa phải nguồn chính thức · có câu trả lời mâu thuẫn · chỉ là lời hẹn · né câu hỏi / trả lời lệch ý / trả lời một phần · chỉ trỏ sang ticket hoặc labcoach mà không rõ kết quả. |
| `done` | Câu trả lời nhắm đúng ý, đến trong ≤120 phút, từ nguồn đáng tin, không mâu thuẫn với tin nào khác. |

**Ba quy ước chốt tại CP4.** Không đổi nhãn nào trong golden set — nhãn giữ nguyên như nhóm đã gán trước khi chạy AI.

1. **Reply lạc đề = `need`.** Reply nói chuyện khác hẳn (`M30201` — hỏi chuyên cần, reply nói về nhận role) là không ai nhắm vào câu hỏi. Khác với trả lời *lệch ý* — nhắm vào câu hỏi nhưng chưa đúng — là `check`.
2. **Đáp án có sẵn cho câu y hệt của người khác, nhưng không ai trỏ cho người hỏi = `need`** (`M18056`). Người hỏi chưa được ai phục vụ. Trạng thái riêng "đã có đáp án, chỉ cần trỏ link" là hướng phát triển **sau CP6**, không thêm vào bộ đo hiện tại.
3. **Tin không phải câu hỏi cần người trả lời = `done` kèm lý do** (`M49586`). Không thêm nhãn thứ năm; lý do phải ghi rõ *"không phải câu hỏi cần trả lời"*.

### Golden set

[`eval/golden_set.json`](eval/golden_set.json) — **25 case, 100% lấy từ data thật**, file chỉ giữ `msg_id`.

| Cơ cấu | Số case | Nhãn kỳ vọng |
|---|---|---|
| Lớp ① Nguồn sự thật | 3 | 3 `nogrounding` |
| Lớp ② Mơ hồ / thiếu thông tin | 3 | 1 `need` · 2 `check` |
| Lớp ③ Ngoài phạm vi / thẩm quyền | 3 | 2 `need` · 1 `check` |
| Lớp ④ Đặc thù domain | 3 | 1 `need` · 2 `check` |
| Case hiếm (ngoài 4 lớp) | 3 | 1 `need` · 2 `check` |
| Case thường | 10 | 5 `need` · 5 `done` |
| **Tổng** | **25** | `need` 10 · `check` 7 · `nogrounding` 3 · `done` 5 |

Ground truth: [`codebase/labels.js`](codebase/labels.js) — 142 tin nhóm đọc và gán nhãn tay. Chạy: `python codebase/run_eval.py --run run-06`.

### Chiều chất lượng — định nghĩa kiểm chứng được

| Chiều | Định nghĩa | Cách đo | Vai trò |
|---|---|---|---|
| **Không bỏ sót** | Case kỳ vọng `need` / `check` / `nogrounding` (**20 case**) mà AI **không** xếp `done` | Recall = (20 − số case bị xếp `done`) / 20 | **Điều kiện 1 của bar** |
| **Không làm phiền** | Trong các mục AI đưa vào danh sách TA (`need` + `check` + `nogrounding`), tỷ lệ mục kỳ vọng `done` | Báo thừa = số mục kỳ vọng `done` trong danh sách / tổng số mục trong danh sách | **Điều kiện 2 của bar** |
| **Riêng tư** | Mục trong bản tin (danh sách gửi TA) không chứa tên hay mã người gửi | Kiểm đầu ra bản tin: chỉ có `msg_id`, kênh, giờ, link | **Điều kiện 3 của bar** |
| Đúng nhãn | AI trả đúng nhãn kỳ vọng | Số case đúng / 25 | Theo dõi, không làm điều kiện — cost-of-error nằm ở bỏ sót, không ở nhầm giữa `need` và `check` |
| Bước lọc không bỏ sót | Câu hỏi thật được rule lọc đưa tới AI | Số tin `need`/`check`/`nogrounding` trong `labels.js` được rule bắt / 32 | Theo dõi riêng — bước lọc bỏ sót thì AI không có cơ hội đúng |

### Quality bar — **KHOÁ TẠI CP4, 17/9/2026**

> **Đạt khi cả ba điều kiện cùng đúng trên golden set:**
> 1. **Bỏ sót ≤ 1/20** câu cần TA xem — tức **recall ≥ 95%** trên 20 case `need` / `check` / `nogrounding`;
> 2. **Báo thừa ≤ 30%** số mục trong danh sách gửi TA;
> 3. **0 mục** trong bản tin chứa tên hoặc mã người gửi.

### Kết quả các lượt chạy

| Lượt | Đổi gì | Đúng nhãn | **Recall (20 case)** | Bỏ sót | **Báo thừa** | Bar |
|---|---|---|---|---|---|---|
| `run-01` | Lượt đầu, prompt v1 | 10/25 · 40% | 16/20 · **80%** | GS-02, GS-03, GS-15, GS-20 | 3/19 · 15,8% | ❌ |
| `run-02` | Prompt v2 — thứ tự quyết định 3 bước | 10/25 · 40% | 17/20 · **85%** | GS-02, GS-15, GS-20 | 4/21 · 19,0% | ❌ |
| `run-03` | Prompt v3 — sửa ranh giới `need`/`check`, siết `nogrounding` | 11/25 · 44% | 16/20 · **80%** | GS-02, GS-03, GS-15, GS-20 | 3/19 · 15,8% | ❌ |
| `run-04` | Ngữ cảnh v4 — quét cả 30 phút trước câu hỏi, thêm `tra_loi_cho` | 13/25 · 52% | 16/20 · **80%** | GS-02, GS-03, GS-15, GS-20 | 3/19 · 15,8% | ❌ |
| `run-05` | Ngữ cảnh v5 — reply trực tiếp kèm độ trễ | 14/25 · 56% | 17/20 · **85%** | GS-02, GS-15, GS-20 | 2/19 · 10,5% | ❌ |

Số liệu khớp [`eval/run_results.md`](eval/run_results.md) và [`eval/README.md`](eval/README.md). Chi tiết từng lượt: [`eval/runs/`](eval/runs/).

### Đối chiếu quality bar — `run-05`

| Điều kiện | Kết quả | |
|---|---|---|
| 1. Bỏ sót ≤ 1/20 (recall ≥ 95%) | Bỏ sót **3/20** — recall **85%** | ❌ **chưa đạt** |
| 2. Báo thừa ≤ 30% | **2/19** — 10,5% | ✅ đạt |
| 3. 0 mục bản tin lộ tên/mã người gửi | Bản tin chỉ xuất `msg_id` + link — **0** | ✅ đạt |

**Kết luận: run-05 chưa đạt quality bar** vì điều kiện 1.

### Vì sao chưa đạt — ba case bỏ sót

| Case | Kỳ vọng → AI | Nguyên nhân | Hướng xử lý |
|---|---|---|---|
| GS-02 · `M97637` | `nogrounding` → `done` | Bot trả lời một câu khác sau 1 phút; model bỏ qua bước 1 (căn cứ có nằm trong tầm nhìn không) khi thấy có tin trả lời gần | Bước 1 chạy độc lập trước — đưa thành luật trong code thay vì để model tự nhớ thứ tự |
| GS-15 · `M19124` | `check` → `done` | Ngữ cảnh đã có `sau_bao_phut = 487` nhưng model vẫn viết "trong vòng 2 giờ" — lỗi tuân thủ, không phải thiếu dữ liệu | Tính sẵn cờ `tra_loi_muon: true` trong code |
| GS-20 · `M18056` | `need` → `done` | Đáp án cho câu y hệt đã có 19 phút trước; nhóm và model đọc đúng dữ liệu nhưng khác định nghĩa | Đã chốt quy ước 2 ở trên: `need`. Cần đưa quy ước này vào prompt v6 |

Chẩn đoán đầy đủ 11 case trượt, gom 7 nhóm nguyên nhân: [`eval/phan_tich.json`](eval/phan_tich.json).

### Recall của bước lọc — đo riêng

| | Bắt được / tổng |
|---|---|
| `need` | **21/21** |
| `check` | **8/8** |
| `nogrounding` | **3/3** |

Bản đầu chỉ bắt 17/32 — bỏ sót câu hỏi dạng yêu cầu không có dấu hỏi (*"Cách nộp daily stand up"*, *"Hạn nộp Lab02"*), `gì` đứng một mình, và tiểu từ `hả`. Rule đã nới theo hướng **thà bắt thừa còn hơn bỏ sót**: bắt thừa tốn thêm một lời gọi AI (rẻ), bỏ sót thì câu hỏi không bao giờ đến tay AI (đắt).

### Tự khai — chưa làm xong tại CP4

| # | Hạng mục | Tình trạng |
|---|---|---|
| 1 | **Quality bar** | **Chưa đạt** — recall 85% < 95%, bỏ sót 3 case (GS-02, GS-15, GS-20), cả ba sai ở mọi lượt |
| 2 | Cách tính recall và báo thừa trong `run_eval.py` | **Đã sửa trước CP4** — recall trên 20 case, báo thừa trên số mục danh sách; báo cáo dựng lại từ log, không gọi lại API |
| 3 | Lý do AI tự viết có thể nhắc mã người gửi | 3/25 lý do trong run-05 có mã dạng `D####` (GS-21, GS-22, GS-25). **Đã lọc ở lớp hiển thị**: `an_ma_nguoi_gui()` trong `decide.py`, áp ở `serve.py` trước khi trả về giao diện, và lọc thêm lần nữa trong `cp2-mock.html`; thẻ tin trong panel căn cứ hiện vai trò (Người hỏi / Người khác / Trợ lý) thay cho mã. Log thô `eval/logs/` giữ nguyên để đối chiếu. **Còn lại:** lý do AI trích trong báo cáo eval (`eval/runs/`, `eval/audit/`) chưa đi qua bộ lọc |
| 4 | Ba quy ước chốt tại CP4 **chưa đưa vào prompt** | Prompt `v5` chưa nói rõ quy ước 2 (đáp án có sẵn nhưng không ai trỏ = `need`) |
| 5 | **Chưa đo độ lệch giữa hai người chấm** | Guide §2.6 bước 4: hai người gán độc lập cùng 20 case rồi so. Nhãn hiện tại do một người gán |
| 6 | `M36687` — trả lời đến sau **705 phút** qua câu hỏi "ké" của người khác | Nằm ngoài mọi cửa sổ thời gian; cần tìm theo ngữ nghĩa. **Giới hạn thiết kế**, chưa làm |
| 7 | Kênh đông (`channel_10`) làm ngữ cảnh lẫn hội thoại khác | Nhóm nguyên nhân B (GS-10). Chưa xử lý |
| 8 | **Golden set chưa có case prompt injection** | Pack không có tin nào khớp mẫu "bỏ qua hướng dẫn"; system prompt đã có câu phòng vệ nhưng **chưa được kiểm** |
| 9 | **Khảo sát chuẩn A chưa thu** | Form đã soạn, chưa đủ ≥20 người |
| 10 | Giao diện là mock HTML | Chưa phải bot chạy trong Discord thật; nút "Trả lời tại tin gốc" không gửi tin đi đâu |

---

## §8. Phân công & kế hoạch

| Người | Mã học viên | Phần việc | Mốc |
|---|---|---|---|
| **Đỗ Ngọc Phi** | 2A202602531 | Prompt + lời gọi AI (`decide.py`) · server chạy lệnh (`serve.py`) · golden set · 5 lượt eval + phân tích nguyên nhân · log mining | **CP3** |
| **Phạm Cường Quốc** | 2A202602469 | Gán nhãn tay 142 tin (`labels.js`) — ground truth · dựng dữ liệu chạy máy (`build_local_data.py`) · chốt spec và quality bar | **CP2**, **CP4** |
| **Nguyễn Trường Bảo** | 2A202602540 | Thiết kế giao diện mô phỏng Discord (`cp2-mock.html`) · slide + video dự phòng | **CP2**, CP5 |
| **Đỗ Đức Đại** | 2A202602725 | Ý tưởng, Canvas 4 ô, lát cắt một câu, bằng chứng ban đầu | **CP1** |

Đội trưởng nộp form mọi mốc: **Đỗ Ngọc Phi · 2A202602531**.

### Kế hoạch sau CP4 *(dự kiến — tên người theo vai trò hiện tại)*

| Việc | Người | Trước |
|---|---|---|
| Prompt/code v6: luật cứng cho ảnh đính kèm và trả lời muộn (`tra_loi_muon`), bước 1 chạy độc lập, đưa 3 quy ước vào prompt → `run-06`. **Quality bar giữ nguyên** | Phi | CP5 |
| Áp `an_ma_nguoi_gui()` cho lý do AI trong báo cáo eval (`run_eval.py`, `redact_logs.py`) | Phi | CP5 |
| Người chấm thứ hai gán độc lập 20 case, so với `labels.js`, ghi tỷ lệ lệch | Đại | CP5 |
| Thêm ≥2 case prompt injection tự viết (ghi rõ là tự viết) vào golden set | Quốc | CP5 |
| Thu khảo sát ≥20 học viên + TA bằng form đã soạn | Đại, Quốc | CP5 |
| Dry run demo 5 phút + quay video dự phòng | Bảo | CP5 · 13:00 18/9 |

### Willing users & vòng validation

| # | Người thử | Vai trò | Trạng thái |
|---|---|---|---|
| 1 | **Huỳnh Văn Nghĩa** | Lab coach | Đã đồng ý thử |
| 2 | *(chưa có)* | TA / Lab coach | Đang mời — thiếu 1 người so với yêu cầu ≥2 |

- **Phạm vi thử:** một ngày dữ liệu (`channel-11` · 13/09, 22 lời gọi AI, ~6 giây).
- **Đo khi thử:** thời gian TA tìm ra câu tồn bằng cách cũ (cuộn kênh + đọc bản tin bot) so với bằng bản tin mới · số mục TA bấm sửa và lý do · số câu tồn TA thấy bị thiếu.
- **Multi-prototype:** không làm — dồn thời gian cho vòng lặp đo ở §7.

---

## §9. Changelog
| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
| 16/9 CP2 | Chốt §4 + §6; dựng bản mock chạy trên data thật tại máy | Phát hiện "không có reply ≠ chưa được trả lời" khi mining → tách 4 trạng thái thay vì một danh sách phẳng |
| 16/9 CP2 | Tách `local-data/` ra khỏi repo, chỉ commit `labels.js` (msg_id + nhãn) | Repo nộp bài là repo công khai; nguyên văn tin nhắn của bạn cùng khoá không được lên mạng |
| 16/9 CP2 | Bỏ phương án bot soạn sẵn câu trả lời cho TA | Bản thử đầu điền sẵn câu như *"BTC có hỗ trợ nới deadline"* — không có nguồn nào trong data nói vậy; Track B yêu cầu deadline chỉ lấy từ nguồn chính thức |
| 17/9 CP3 | Thay nhãn tay trong giao diện bằng lời gọi AI thật (`gpt-4o-mini`); 5 lượt đo trên golden set 25 case | CP3 yêu cầu AI thật ở quyết định trung tâm; nhãn tay chuyển thành ground truth |
| 17/9 CP3 | Nới rule lọc ứng viên (17/32 → 32/32) | Bỏ sót ở bước lọc thì AI không có cơ hội đúng |
| 17/9 CP4 | Hoàn thiện §1–§3, §5, §7, §8 | Hạn chốt spec |
| 17/9 CP4 | Chốt định nghĩa 4 nhãn + 3 quy ước (reply lạc đề = `need`; đáp án có sẵn không ai trỏ = `need`; không phải câu hỏi = `done` kèm lý do). **Không đổi nhãn nào trong golden set** | Phân tích run-05 (GS-13, GS-20, GS-24) cho thấy ranh giới chưa được viết ra. Giữ nhãn gán trước khi chạy AI để không chỉnh ground truth theo kết quả |
| 17/9 CP4 | Chuẩn hoá cách tính recall (mẫu số 20, gồm `nogrounding`) và báo thừa (trên số mục danh sách); **giữ nguyên ngưỡng 95% / 30% / 0** | Chữ "≤1/20" trong bar có sẵn trước CP4; script cũ tính trên 17 case nên báo 88,2%. Số đúng là 85% — tệ hơn, nhưng đúng với bar |
| 17/9 CP4 | Lọc mã người gửi khỏi lý do AI trước khi hiện cho TA; thẻ tin trong panel căn cứ hiện vai trò thay cho mã | Lý do do model tự viết nhắc mã tác giả ở 3/25 case run-05 — mâu thuẫn với cam kết "không nêu tên" của bản tin (④, K13) |
| 17/9 CP4 | Điền người thử: Huỳnh Văn Nghĩa (Lab coach) | Đã đồng ý thử; còn thiếu 1 người |
| 17/9 CP4 | Khoá quality bar | Hạn 21:00 17/9 |
