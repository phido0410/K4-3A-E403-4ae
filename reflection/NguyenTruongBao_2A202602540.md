# Báo Cáo Reflection Cá Nhân — Hackathon AI Batch 04

## Thông Tin Thành Viên
- **Họ và tên:** Nguyễn Trường Bảo
- **Mã học viên:** 2A202602540
- **Nhóm:** 4AE (Lớp 3A · Phòng thi E403 · Cụm 4)
- **Đề tài:** Track B2 — Trợ lý Discord hỗ trợ Trợ giảng (Sản phẩm: **AI hỗ trợ TA tìm các câu hỏi bị missing**)
- **Lát cắt sản phẩm:** *Một TA · cuối ngày muốn biết còn câu nào bị miss · AI quyết định mỗi câu hỏi đã thực sự được giải đáp chưa · TA nhận danh sách câu bị miss kèm link tới tin gốc, không nêu tên, bấm vào là trả lời đúng chỗ.*

---

## 1. Tôi Đã Tham Gia Vào Phần Nào? (Dấu Vết Cụ Thể Trong Repo)

Trong dự án của nhóm 4AE, tôi chịu trách nhiệm chính về **Thiết kế Trải nghiệm Người dùng (UI/UX Mockup), Trực quan hoá Hệ thống Slide 6 trang và Sản xuất Video Demo Dự Phòng (CP2, CP5)**.

| Hạng mục công việc | Việc cụ thể tôi đã làm | Artifact / File tương ứng trong Repo | Kết quả & Đóng góp cho nhóm |
| :--- | :--- | :--- | :--- |
| **Giao diện mô phỏng Discord (Mockup UI)** | Thiết kế và hiện thực hóa toàn bộ giao diện mô phỏng Discord hoàn chỉnh: danh sách kênh, khung chat, thẻ bản tin của bot và panel căn cứ. *(Ô gõ lệnh gạch chéo `/question_unanswer` và phần nối bản tin thời gian thực qua SSE do Phi bổ sung ở CP3 trên nền giao diện này.)* | [`codebase/cp2-mock.html`](../codebase/cp2-mock.html) (~77 KB) | Giúp nhóm có prototype bấm được end-to-end từ CP2; ban giám khảo và người dùng thử có cảm giác như đang thao tác trực tiếp trong Discord thật. |
| **Bản tin AI & Căn cứ Grounding** | Thiết kế bản tin phân loại câu hỏi (`Cần trả lời`, `Cần kiểm tra`, `Đã được trả lời`) và panel bên phải hiển thị căn cứ trích dẫn AI Grounding khi bấm vào từng câu hỏi. | [`codebase/cp2-mock.html`](../codebase/cp2-mock.html) (khung `#digest-card`, `#grounding-panel`) | Thể hiện trực quan nguyên tắc **HAX G11 (Giải thích có căn cứ)**: trích dẫn nguyên văn mã tin nhắn gốc, lời giải thích tiếng Việt minh bạch. |
| **Cơ chế Human-in-the-Loop** | Hiện thực tương tác cho phép TA trực tiếp can thiệp: nút bấm đổi nhãn, chọn lý do sửa đổi, lưu audit log, gắn huy hiệu xanh `"TA đã sửa"` và hiển thị thông báo toast xác nhận. | [`codebase/cp2-mock.html`](../codebase/cp2-mock.html) (hàm `saveCorrection()`) | Hiện thực hóa nguyên tắc **HAX G9 (Sửa đổi dễ dàng)**; đảm bảo an toàn tuyệt đối vì AI chỉ đóng vai trò Augment (hỗ trợ), TA nắm toàn quyền quyết định. |
| **Bảo vệ danh tính (Privacy Guard)** — *Phi thực hiện ở CP3, tôi kiểm thử trên giao diện* | Che mã học viên dạng `D####` thành bí danh ổn định `Học viên NN` ở khung chat, bản tin và panel căn cứ. Phần tôi làm là rà lại toàn bộ màn hình để tìm chỗ còn lộ mã. | [`codebase/cp2-mock.html`](../codebase/cp2-mock.html), [`spec.md`](../spec.md#L359) | Đạt tuyệt đối điều kiện 3 của Quality Bar: **0 rò rỉ danh tính người gửi** trên toàn bộ giao diện. |
| **Hệ thống Slide 6 trang chuẩn Sân Khấu** | Lập trình bằng HTML/CSS và xuất bản bộ slide thuyết trình 6 trang chuẩn tỉ lệ 16:9, Dark mode cao cấp; tối ưu typography lớn (+25%) cho máy chiếu hội trường; tái cấu trúc Slide 1 (bố cục Top-Bottom); crop/zoom cận cảnh Slide 3. | [`validation/slides.html`](../validation/slides.html), [`demo-slides.pdf`](../demo-slides.pdf) | Slide đạt chuẩn chuyên nghiệp, không vỡ layout, số liệu đập vào mắt người xem từ cự ly > 10m; đáp ứng chuẩn xác quy định 6 trang của `02-guide.md §5.1`. |
| **Video Demo dự phòng & Kịch bản Pitch** | Xây dựng kịch bản thuyết trình phân vai cho 4 thành viên; quay và chuẩn bị sẵn video demo màn hình kịch bản thao tác thật (1 case chuẩn + 1 case chỗ khó có TA can thiệp) phòng ngừa sự cố mạng lúc pitch. | [`demo-slides.pdf`](../demo-slides.pdf), Checklist CP5 | Đảm bảo nhóm không bị trừ điểm kỹ thuật tại CP5 và buổi pitch diễn ra mượt mà. |

**Dấu tay rõ nét nhất của tôi trong sản phẩm:**
Bố cục và toàn bộ phần nhìn của [`codebase/cp2-mock.html`](../codebase/cp2-mock.html) cùng bộ slide trình chiếu. Cái giám khảo nhìn thấy trên màn hình — cây kênh, khung chat, thẻ bản tin ba khối, panel trích dẫn căn cứ, nút cho TA sửa nhãn — là do tôi dựng và tinh chỉnh.

**Phần trong file này không phải tôi viết:** lớp nối SSE (`runCommand()`), gợi ý lệnh bấm Tab, che mã người gửi và lọc kênh theo server — đều là bản vá của Phi ở CP3. Tôi khai rõ để không nhận vơ phần mình không giải thích được (xem mục 4).

---

## 2. AI Đã Hỗ Trợ Tôi Như Thế Nào?

Trong quá trình xây dựng giao diện và slide, tôi đã tận dụng các công cụ AI (Claude, Cursor, ChatGPT) như một người cộng sự kỹ thuật:

- **Điểm AI hỗ trợ xuất sắc:**
  - **Tạo khung giao diện (Boilerplate):** AI giúp sinh nhanh bảng mã màu HSL và các token CSS chuẩn Dark mode của Discord (màu nền `#313338`, `#2b2d31`, `#1e1f22`, font monospace `JetBrains Mono` cho mã tin nhắn).
  - **Chuyển đổi ý tưởng sang CSS Layout:** Khi tôi muốn chuyển Slide 1 từ bố cục 2 cột cũ sang bố cục Top-Bottom (Hero card JTBD ở trên, 3 metric card nằm ngang ở dưới), AI đã hỗ trợ tôi viết nhanh cú pháp CSS Grid và Flexbox responsive rất chuẩn xác.
- **Điểm hạn chế của AI và con người phải trực tiếp can thiệp:**
  - **Ảo giác về bố cục in ấn / màn chiếu:** Khi chuyển từ HTML sang PDF để trình chiếu, AI không lường trước được việc font chữ hiển thị trên máy chiếu hội trường sẽ rất bé nếu dùng kích thước thông thường (14-16px). Tôi phải tự mình rà soát, đo lường và cưỡng bức scale lại toàn bộ typography (+20% đến +30%), đồng thời tính toán lại padding trần-sàn (`46px 72px 40px 72px`) để không bị tràn khung hình 1080px.
  - **Logic nghiệp vụ tương tác phức tạp:** AI thường sinh các hàm xử lý dữ liệu giả (hardcoded mock data). Tôi phải tự tay kết nối luồng SSE từ backend `serve.py`, viết logic lưu vết audit khi TA bấm đổi nhãn, và đảm bảo thông điệp phản hồi luôn tuân thủ nguyên tắc HAX Toolkit (không giấu lỗi, có nút hoàn tác/sửa đổi).

---

## 3. Một Bài Học Sâu Sắc Từ Case Thất Bại Của Nhóm

Trong quá trình đo lường 25 ca kiểm thử trên Golden Set, một case thất bại khiến tôi thay đổi hoàn toàn tư duy thiết kế sản phẩm AI là **ca GS-15 (Mã tin M19124)**:

- **Tình huống thực tế:** Học viên hỏi một câu hỏi kỹ thuật. Câu trả lời chính xác đã xuất hiện, nhưng đến sau câu hỏi tới **487 phút** (hơn 8 tiếng đồng hồ).
- **Thất bại của AI:** Mô hình AI nhầm lẫn timestamp giữa các tin nhắn trung gian và kết luận sai lầm rằng *"câu hỏi đã được trả lời trong vòng 2 giờ"* → tự ý xếp nhãn `done` (đã xong). Nếu bot tự động hoạt động, câu hỏi này sẽ bị ẩn đi, học viên phải chờ đợi trong vô vọng mà TA không hề hay biết.
- **Bài học thiết kế giao diện rút ra cho bản thân:**
  1. **Không bao giờ thiết kế hệ thống AI tự động hóa hoàn toàn (Autonomous) trong bài toán hỗ trợ con người:** Ban đầu tôi từng nghĩ đến ý tưởng cho bot tự động gửi câu trả lời hoặc tự đóng ticket câu hỏi. Nhưng sau khi chứng kiến ca GS-15 và GS-20 (AI nhầm lẫn ngữ cảnh đa luồng), tôi nhận ra rằng AI rất dễ bị "đánh lừa" bởi độ trễ thời gian hoặc sự phân mảnh của phòng chat.
  2. **Giá trị cốt lõi của giao diện là "Tạo điều kiện cho con người sửa sai" (Human-in-the-loop):** Tôi lập tức thiết kế panel căn cứ AI Grounding (HAX G11) để TA luôn nhìn thấy lý do tại sao AI đưa ra nhãn đó, kèm theo nút bấm sửa nhãn tức thì (HAX G9). Việc thừa nhận AI có thể sai và trao quyền tối thượng cho TA kiểm soát có giá trị thực tiễn cao hơn gấp nhiều lần việc cố tạo ra một giao diện hào nhoáng giả vờ AI đúng 100%.

---

## 4. Cam Kết Tự Bảo Vệ Trước Ban Giám Khảo (Vibe-Coding Rule Check)

*Quy tắc vibe-coding (`04-rubric.md`): bị giám khảo hỏi phần có tên mình mà không giải thích được → **0 điểm phần cá nhân liên quan**. Vì vậy phần này khai đúng mức tôi nắm, không khai quá — chỗ nào chỉ nắm một nửa tôi ghi rõ là một nửa.*

### Tôi giải thích được ngay, không cần mở file

- **Bố cục giao diện mô phỏng Discord:** cây server và kênh bên trái, khung chat ở giữa, thẻ bản tin của bot, panel căn cứ trượt ra bên phải. Vì sao dựng theo đúng Discord thật: TA không phải học giao diện mới, và giám khảo nhìn là hiểu ngay đây sẽ sống ở đâu.
- **Vì sao bản tin tách 3 khối** `Cần trả lời` / `Cần kiểm tra` / `Đã được trả lời`, và vì sao khối thứ ba **gập lại mặc định** — TA cuối ca chỉ cần nhìn việc còn phải làm, không cần cuộn qua thứ đã xong.
- **Luồng thao tác của TA:** bấm vào một câu hỏi → panel căn cứ mở ra kèm trích tin gốc → nhảy tới đúng tin trong khung chat → đổi nhãn nếu AI sai → hiện huy hiệu *"TA đã sửa"*. Tôi thao tác được toàn bộ luồng này trên sân khấu.
- **Bộ slide:** vì sao chọn tỉ lệ 16:9, cỡ chữ và độ tương phản đặt theo khoảng cách nhìn trên 10m, và vì sao Slide 3 phải crop cận cảnh thay vì chụp cả màn hình.

### Tôi chỉ nắm khoảng 50% — sẽ nói thẳng là chưa chắc

- **Cơ chế SSE.** Tôi hiểu ở mức nguyên lý: máy chủ đẩy về lần lượt `quet` → `ung_vien` → `tien_do` → `xong`, giao diện vẽ dần thay vì đứng im chờ chạy xong. Nhưng phần nối `EventSource` trong hàm `runCommand()` là **Phi ghép vào ở CP3, không phải tôi viết**. Bị hỏi vào code đó, tôi nói đúng như vậy và chuyển câu hỏi cho Phi.
- **Ba bản vá ở CP3 nằm trong file mang tên tôi nhưng không do tôi làm:** che mã người gửi (`biDanh()` / `anMa()`), gợi ý lệnh bấm Tab, và lọc kênh theo đúng server đang xem. Tôi nắm được **ý tưởng** và kiểm được kết quả trên màn hình, nhưng không nắm code.

Tôi khai rõ ranh giới này ngay từ đầu, vì `cp2-mock.html` mang tên tôi mà bên trong có phần không phải tôi viết — nhận vơ rồi tắc giữa chừng thì mất điểm nặng hơn là nói thẳng.

### Ngoài phạm vi của tôi

`decide.py`, `run_eval.py`, prompt, golden set (Phi) · 142 nhãn tay (Quốc) · Canvas 4 ô (Đại).
