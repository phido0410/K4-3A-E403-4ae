# Báo Cáo Reflection Cá Nhân — Hackathon AI Batch 04

## Thông Tin Thành Viên
- **Họ và tên:** Phạm Cường Quốc
- **Mã học viên:** 2A202602469
- **Nhóm:** 4AE (Lớp 3A · Phòng thi E403 · Cụm 4)
- **Đề tài:** Track B2 — Trợ lý Discord hỗ trợ Trợ giảng (Sản phẩm: **AI hỗ trợ TA tìm các câu hỏi bị missing**)
- **Lát cắt sản phẩm:** *Một TA · cuối ngày muốn biết còn câu nào bị miss · AI quyết định mỗi câu hỏi đã thực sự được giải đáp chưa · TA nhận danh sách câu bị miss kèm link tới tin gốc, không nêu tên, bấm vào là trả lời đúng chỗ.*

---

## 1. Tôi Đã Tham Gia Vào Phần Nào? (Dấu Vết Cụ Thể Trong Repo)

Trong dự án của nhóm 4AE, tôi chịu trách nhiệm chính về **Thiết lập Ground Truth (Gán nhãn chuẩn), Xây dựng Tài liệu AI Spec và Khóa Cứng Quality Bar (CP2, CP4)**.

| Hạng mục công việc | Việc cụ thể tôi đã làm | Artifact / File tương ứng trong Repo | Kết quả & Đóng góp cho nhóm |
| :--- | :--- | :--- | :--- |
| **Gán nhãn độc lập 142 tin (Ground Truth)** | Đọc tay từng tin nhắn trong 142 tin Discord thật từ data pack; phân tích ngữ cảnh trao đổi và gán nhãn ground truth (`need`, `check`, `nogrounding`, `done`). | [`codebase/labels.js`](../codebase/labels.js) (~10.2 KB) | Thiết lập "thước đo chuẩn" không thiên vị để đánh giá khách quan độ chính xác của AI qua từng lượt chạy (không nạp file này vào giao diện để đảm bảo tính độc lập). |
| **Soạn thảo AI Spec toàn diện (§1 - §9)** | Chủ trì biên soạn toàn bộ tài liệu đặc tả kỹ thuật sản phẩm theo mẫu chuẩn `03-ai-spec-template.md`: định nghĩa bài toán, phân tích 3 ứng viên, phát biểu lát cắt 1 câu, thiết kế mức tự động hóa Augment, áp dụng 4 nguyên tắc HAX/PAIR. | [`spec.md`](../spec.md) (~35.7 KB) | Đem lại cho nhóm 15/15 điểm khối **R2 (Lát cắt & Thiết kế)**; giúp toàn đội thống nhất ranh giới kỹ thuật từ CP2 đến khi hoàn thành. |
| **Hệ thống hóa Taxonomy 4 lớp chỗ khó & 8 kịch bản** | Xây dựng taxonomy phân loại 4 lớp chỗ khó cốt lõi (① Nguồn sự thật bị giới hạn, ② Ngữ cảnh phân mảnh đa luồng, ③ Ranh giới nhãn mơ hồ, ④ Ràng buộc thời gian domain); xây dựng bảng 8 kịch bản kiểm thử chi tiết kèm hành vi mong muốn. | [`spec.md`](../spec.md#L156) (§5 & §6) | Đem lại 11/11 điểm tối đa ở khối **R3 (Chỗ khó & Kịch bản rủi ro)**; định hướng chính xác cho Phi xây dựng Golden Set. |
| **Thiết lập & Khóa cứng Quality Bar (CP4)** | Thiết lập 3 tiêu chí đo lường định lượng và cam kết ngưỡng đạt trước thời hạn 21:00 17/9: **Recall ≥ 95.0%**, **False Positive ≤ 30.0%**, **Privacy rò rỉ = 0**. | [`spec.md`](../spec.md#L272) (§7) | Khóa chuẩn "đạt" bằng con số đúng hạn quy định; bảo vệ cam kết chất lượng không bao giờ bị nới lỏng hay sửa đổi sau CP4. |
| **Xử lý dữ liệu chạy máy & Privacy** | Viết script `build_local_data.py` làm sạch dữ liệu; mở rộng cam kết bảo vệ danh tính: lọc bỏ toàn bộ mã người gửi `D####` ra khỏi lý do do AI sinh ra và khung hiển thị. | [`codebase/build_local_data.py`](../codebase/build_local_data.py), [`spec.md`](../spec.md#L355) (Changelog) | Đảm bảo hệ thống vận hành trơn tru trên máy cục bộ mà tuyệt đối không vi phạm bảo mật dữ liệu của khoá học. |

**Dấu tay rõ nét nhất của tôi trong sản phẩm:**
Bộ dữ liệu chuẩn [`codebase/labels.js`](../codebase/labels.js) và toàn bộ tài liệu kiến trúc [`spec.md`](../spec.md). Mọi ranh giới về định nghĩa nhãn, taxonomy 4 lớp chỗ khó và cam kết Quality Bar mà nhóm thuyết trình trước Ban Giám khảo đều do tôi trực tiếp chốt và bảo vệ.

---

## 2. AI Đã Hỗ Trợ Tôi Như Thế Nào?

Trong quá trình soạn thảo Spec và phân tích dữ liệu, tôi sử dụng AI để hỗ trợ tra cứu và đối chiếu:

- **Điểm AI hỗ trợ tốt:**
  - **Tra cứu nguyên tắc HAX Toolkit và PAIR Guidebook:** AI hỗ trợ tra cứu nhanh định nghĩa 18 nguyên tắc của Microsoft HAX và các chỉ dẫn trong Google PAIR, giúp tôi chọn ra 4 nguyên tắc phù hợp nhất (G1, G10, G9, G11) để đưa vào mục §4 của Spec.
  - **Phát thảo các tình huống edge-case:** AI gợi ý một số kịch bản rủi ro trong môi trường chat nhóm (ví dụ: học viên hỏi ké, câu trả lời bị ngắt quãng), giúp tôi hoàn thiện bảng 8 kịch bản ở mục §6.
- **Điểm hạn chế của AI và con người phải trực tiếp can thiệp:**
  - **AI không thể tự tạo ra Ground Truth:** Khi tôi thử đưa một số tin nhắn mẫu cho LLM tự gán nhãn, LLM thường đưa ra kết quả không nhất quán giữa các lần chạy và rất dễ bị "đánh lừa" khi thấy có tin nhắn xuất hiện sau đó. Tôi nhận ra rằng: **Không bao giờ được dùng AI để gán nhãn chuẩn nhằm chấm điểm chính AI**. Tôi đã dành hàng giờ đồng hồ đọc tay toàn bộ 142 tin nhắn thật, đối chiếu từng dòng thời gian để tự mình gán nhãn thủ công cho `labels.js`.
  - **Định nghĩa ranh giới nhãn mơ hồ:** Ban đầu, ranh giới giữa `need` và `check` còn mờ nhạt. Khi phân tích lượt chạy Run-05, tôi phát hiện ra 3 trường hợp mâu thuẫn (GS-13, GS-20, GS-24). Tôi đã phải trực tiếp bổ sung 3 quy ước ranh giới chặt chẽ vào Spec: (1) Reply lạc đề = `need`; (2) Đáp án có sẵn trong kênh nhưng không ai chỉ = `need`; (3) Tin không phải câu hỏi = `done` kèm giải thích.

---

## 3. Một Bài Học Sâu Sắc Từ Case Thất Bại Của Nhóm

Bài học lớn nhất đối với tôi không nằm ở một dòng code, mà nằm ở **Quyết định đối diện với thất bại đo lường tại Run-06**:

- **Tình huống thực tế:** Khi chạy kiểm thử đợt cuối (Run-06) trên 20 ca cần TA xem xét, AI chỉ nhận diện đúng 17 ca, bỏ sót 3 ca nguy hiểm (GS-02, GS-15, GS-20) → **Recall thực tế đạt 85.0%**, trong khi Quality Bar nhóm đã cam kết tại CP4 là **≥ 95.0%**.
- **Cám dỗ "làm đẹp số liệu":** Lúc đó, nhóm chỉ cần sửa nhẹ nhãn của 2 ca trong Golden Set từ `need` sang `check` hoặc hạ Quality Bar xuống 80% là bảng kết quả sẽ hiện toàn màu xanh "ĐẠT CHUẨN".
- **Bài học về đạo đức và tư duy sản phẩm AI:**
  1. **Tuyệt đối không sửa chuẩn sau khi đã chốt:** Quality Bar đã cam kết tại hạn chốt spec (21:00 17/9) là lời hứa kỹ thuật. Nếu thấy kết quả thấp mà vội vàng sửa bar cho đẹp thì việc đo lường trở nên vô nghĩa.
  2. **Giá trị của việc "Dũng cảm thừa nhận hệ thống chưa đạt bar":** Tôi đã quyết định giữ nguyên toàn bộ nhãn gốc và công khai trung thực con số 85.0% trên Slide 4. Thay vì che giấu, nhóm biến 3 ca thất bại thành tâm điểm phân tích sâu ở Slide 5 và đưa ra kế hoạch khắc phục rõ ràng ở Slide 6. Khi sản phẩm AI phục vụ con người, việc thấu hiểu ranh giới sai sót của mô hình để thiết kế lưới an toàn quan trọng hơn nhiều việc tạo ra ảo tưởng về một mô hình hoàn hảo 100%.

---

## 4. Cam Kết Tự Bảo Vệ Trước Ban Giám Khảo (Vibe-Coding Rule Check)

*Quy tắc vibe-coding (`04-rubric.md`): bị giám khảo hỏi phần có tên mình mà không giải thích được → **0 điểm phần cá nhân liên quan**. Vì vậy phần này khai đúng mức tôi nắm, không khai quá — chỗ nào chỉ nắm một nửa tôi ghi rõ là một nửa.*

### Tôi giải thích được ngay, không cần mở file

- **Định nghĩa 4 nhãn** `need` / `check` / `nogrounding` / `done` và **3 quy ước** chốt ở CP4: reply lạc đề vẫn tính `need`; đáp án có sẵn mà không ai trỏ cho người hỏi vẫn tính `need`; tin không phải câu hỏi thì `done` kèm lý do.
- **Vì sao mẫu số recall là 20 chứ không phải 17.** Bar viết "bỏ sót ≤ 1/20", mà `need` + `check` + `nogrounding` = 21 + 8 + 3 → trong golden set là đúng 20 ca. Bản cũ tính theo mẫu số 17 nên ra 88,2%, con số thật là **85%**. Tôi là người phát hiện lỗi này trước hạn CP4 và yêu cầu đo lại.
- **Vì sao báo thừa lấy mẫu số 19:** đó là số mục thật sự xuất hiện trên bản tin gửi TA, không phải 25. → 2/19 = **10,5%**.
- **Vì sao nhóm chọn augment thay vì automate**, dựa trên cost-of-error lệch hẳn một bên: báo thừa tốn TA 10 giây, bỏ sót thì học viên bị lờ và không ai biết.
- **Cơ sở gán nhãn cho 32 ca** `need`/`check`/`nogrounding` và **25 ca golden set** — mỗi ca đều có trường `reason` do tôi viết trong `labels.js`.
- **Nguyên tắc tôi giữ:** không sửa một nhãn nào sau khi đã thấy kết quả AI. Chỉnh ground truth theo output là tự lừa mình.

### Tôi chỉ nắm khoảng 50% — sẽ nói thẳng là chưa chắc

- **"Bất kỳ tin nào trong 142 tin" — tôi không nhớ hết.** 110 ca `done` tôi nhớ theo **nhóm lý do** (có tin trả lời đúng ý trong 4 giờ · không phải câu hỏi cần người trả lời · trùng câu đã hỏi trước đó), chứ không thuộc lòng từng mã tin. Được mở `labels.js` ra thì tôi trả lời chính xác từng ca; hỏi chay thì tôi chỉ chắc ở 32 ca cần TA xem và 25 ca golden set.
- **Code Python.** Tôi đọc được luồng `decide.py` và `run_eval.py` ở mức biết chỗ nào tính ra con số nào, nhưng **không tự viết lại được**. Phần đó Phi làm.

### Một câu tôi rút lại vì nó sai

Bản trước tôi viết Human-in-the-loop *"ngăn chặn hoàn toàn rủi ro"*. **Câu đó sai và tôi rút lại.**

HITL chỉ chặn được **báo thừa**: mục sai vẫn hiện lên bản tin nên TA còn nhìn thấy mà bỏ qua. Nó **không chặn được bỏ sót**: ba ca GS-02, GS-15, GS-20 bị AI xếp `done` thì không lên bản tin, TA không nhìn thấy thì không có gì để sửa. Đây đúng là lỗ hổng còn lại của thiết kế, và cũng là lý do nhóm đặt bar recall tới 95% rồi tự khai là **chưa đạt**.

### Ngoài phạm vi của tôi

Prompt và code gọi LLM (Phi) · giao diện mock (Bảo) · Canvas 4 ô (Đại).
