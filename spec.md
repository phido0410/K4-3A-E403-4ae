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
**Mock.** Flow bấm hết được, dữ liệu là fixture tự sinh.
| Phần | CP2 | CP3 |
|---|---|---|
| Flow 4 màn, phân nhóm, panel giải thích, nút sửa | thật (đã chạy) | giữ nguyên |
| **Quyết định "đã được giải đáp chưa"** | **mock — kịch bản dựng sẵn** | **lời gọi AI thật**, log trong `eval/` |
| Đọc tin từ Discord | fixture | đọc từ `k4_messages.csv` tại máy cá nhân |
| Link tới tin gốc | mock (alert) | link thật |

### Automation: **augment**
AI lập danh sách, **TA quyết định**. Cost-of-error lệch hẳn một bên:
- **Báo thừa** một câu đã được trả lời → TA mất ~10 giây bỏ qua. Rẻ, TA tự thấy ngay.
- **Bỏ sót** một câu thật sự bỏ ngỏ → học viên bị lờ, không ai biết để sửa. Đắt, và không tự lộ ra.

→ Thiết kế ưu tiên **không bỏ sót**, chấp nhận báo thừa, và luôn có người duyệt trước khi chạm tới học viên.

### §4b. Nguyên tắc đã áp dụng
| Nguyên tắc | Áp cụ thể vào đâu trong prototype |
|---|---|
| **G1** · Làm rõ hệ thống làm được gì | Dòng phạm vi ngay dưới tên sản phẩm: nói rõ bản tin làm gì và **không** nhắn cho học viên |
| **G2** · Làm rõ nó làm tốt đến đâu | Chân bản tin khai trước: bản tin bỏ sót được vì chỉ đọc kênh công khai |
| **G10** · Thu hẹp phạm vi khi nghi ngờ | Hai nhóm riêng "Cần bạn xác nhận" và "Không đủ căn cứ" — máy không chắc thì nói không chắc, không xếp bừa vào nhóm bỏ ngỏ |
| **G11** · Giải thích vì sao | Panel "Vì sao câu này ở đây": liệt kê đúng căn cứ đã dùng + mức chắc chắn |
| **G9** · Sửa dễ dàng | Nút "Có người trả lời rồi" / "Không phải câu hỏi" ngay trên từng mục, một cú bấm |
| **G17** · Quyền kiểm soát tổng | Màn đóng bản tin đếm rõ **0 tin đã gửi học viên** |

*Bật nút "Hiện chú thích nguyên tắc" trong bản mock để thấy vị trí từng nguyên tắc trên giao diện.*

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
| **Happy path** | Nhóm "Chắc chắn còn bỏ ngỏ" — mức chắc chắn 85–92%, kèm căn cứ và thời gian đã trôi. TA bấm "Tôi nhận trả lời câu này". |
| **Low-confidence (②)** | Nhóm riêng "Cần bạn xác nhận" — ví dụ reply là *"em ké câu hỏi ạ"*, chắc chắn 38%. Máy **nói ra chỗ nó phân vân** thay vì xếp bừa. |
| **Failure / không căn cứ (①)** | Nhóm "Không đủ căn cứ để kết luận" — tin nhắc tới tin ngoài phạm vi thu thập. Máy ghi *"không kết luận được"*, **không đoán**, đẩy sang cho người xem. |
| **Correction (user sửa)** | Hai nút "Có người trả lời rồi" / "Không phải câu hỏi" trên từng mục; mục biến khỏi bản tin và được đếm vào "bạn sửa lại máy" ở màn đóng. |
| **Bị đòi ngoài phạm vi (③)** | Câu hỏi cá nhân vẫn được liệt kê, nhưng bản tin không tra cứu hộ — TA tự xử lý ở Discord. |
| **Case đặc thù domain (④)** | Bản tin **không hiện tên người hỏi**, chỉ mã tin + link. Bản tin gửi vào kênh riêng của TA, không đăng công khai. |

---

## §7. Kiểm thử
- **Đơn vị một case:** một câu hỏi + ngữ cảnh quanh nó → nhãn `còn bỏ ngỏ / đã được trả lời / không phải câu hỏi`.
- **Quality bar (dự kiến, chốt tại CP4):** *"Đạt khi bỏ sót ≤1/20 câu thật sự bỏ ngỏ (recall ≥95%), và ≤30% mục trong bản tin là báo thừa, và 0 mục lộ tên người."*
- Golden set ≥20 case trong `eval/` — hạt giống là 27 câu đã lọc, gán nhãn tay bởi 2 người độc lập.

## §8. Phân công & kế hoạch
*(điền tên — bắt buộc cho R7)* spec · evidence/mining · prompt + AI call · flow/UI · golden set + eval · demo

## §9. Changelog
| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
| 16/9 CP2 | Chốt §4 + §6, dựng bản mock 4 màn | Phát hiện "không có reply ≠ chưa được trả lời" khi mining → tách riêng nhóm "cần xác nhận" và "không đủ căn cứ" thay vì một danh sách phẳng |
