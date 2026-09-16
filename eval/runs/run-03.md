# Ket qua chay golden set — luot `run-03`

- **Model:** `gpt-4o-mini` · prompt `v3`
- **Luc chay:** 16/09/2026 23:47
- **Bo test:** `eval/golden_set.json` — 25 case
- **Ground truth:** `codebase/labels.js` (nhom doc tay 142 tin)
- **Log tung case:** `eval/logs/run-03/`

## 1. Tong hop

| Chi so | So |
|---|---|
| Tong case | 25 |
| Dat | 11 |
| Truot | 14 |
| **Ty le dat** | **44.0%** |
| Bo sot cau con ton (xep nham thanh `done`) | **2/17** |
| Recall tren nhom can TA xem | **88.2%** |
| Bao thua (`done` bi xep thanh can xem) | 3 |

> Ty le dat chung khong phai chi so quan trong nhat. Bo sot dat hon bao thua nhieu lan:
> bao thua ton cua TA 10 giay, bo sot thi hoc vien bi bo roi ma khong ai biet.

## 2. Ket qua theo lop cho kho

| Lop | Case | Dat | Ty le |
|---|---|---|---|
| ① Nguon su that | 3 | 1 | 33% |
| ② Mo ho / thieu thong tin | 3 | 1 | 33% |
| ③ Ngoai pham vi / tham quyen | 3 | 2 | 67% |
| ④ Dac thu domain | 3 | 1 | 33% |
| Case thuong | 10 | 5 | 50% |
| Case hiem | 4 | 1 | 25% |

## 3. Ma tran nham lan

| ky vong \ AI tra ve | need | check | nogrounding | done |
|---|---|---|---|---|
| **need** | 7 | 2 | · | 1 |
| **check** | 5 | 1 | · | 1 |
| **nogrounding** | · | · | 1 | 2 |
| **done** | 1 | 2 | · | 2 |

## 4. Tung case

| Case | Tin | Lop | Ky vong | AI tra ve | Dat | Ly do AI dua ra |
|---|---|---|---|---|---|---|
| GS-01 | `M80884` | ① | nogrounding | nogrounding | dat | Câu hỏi trỏ tới một người cụ thể mà không có nội dung nào trong ngữ cảnh để trả lời, chỉ là yêu cầu nhắc nhở m |
| GS-02 | `M97637` | ① | nogrounding | done | **TRUOT** | Câu hỏi đã được trả lời đầy đủ bởi BOT trong vòng 2 giờ, cung cấp thông tin chi tiết về file hướng dẫn mà ngườ |
| GS-03 | `M51326` | ① | nogrounding | done | **TRUOT** | Câu hỏi đã được trả lời đầy đủ và đúng ý trong vòng 2 giờ từ người dùng D6587. Tin trả lời cung cấp thông tin  |
| GS-04 | `M33885` | ② | need | need | dat | Câu hỏi chưa được ai trả lời và không có ai nhắc đến nội dung câu hỏi trong các tin nhắn gần đây. Do đó, cần p |
| GS-05 | `M00553` | ② | check | need | **TRUOT** | Câu hỏi chưa được giải đáp vì chỉ có một tin nhắn hẹn hỏi lại mà không có câu trả lời cụ thể nào cho câu hỏi.  |
| GS-06 | `M54679` | ② | check | need | **TRUOT** | Câu hỏi chưa được ai trả lời, và không có ai nhắc đến nội dung câu hỏi trong các tin nhắn gần đây. |
| GS-07 | `M30246` | ③ | need | need | dat | Câu hỏi chưa được ai trả lời, không có phản hồi nào từ người khác trong kênh. Cần chờ xem có ai trả lời trong  |
| GS-08 | `M27566` | ③ | need | need | dat | Câu hỏi chưa được ai trả lời, không có tin nhắn nào nhắm vào nội dung câu hỏi. Do đó, cần phải chờ đợi thêm để |
| GS-09 | `M88027` | ③ | check | need | **TRUOT** | Câu hỏi chưa được giải đáp vì không có ai trả lời trực tiếp cho câu hỏi này. Các tin nhắn trong kênh không liê |
| GS-10 | `M72484` | ④ | need | check | **TRUOT** | Câu hỏi về hạn nộp Lab02 chưa được giải đáp rõ ràng. Có nhiều tin nhắn liên quan đến việc nộp lab muộn nhưng k |
| GS-11 | `M18676` | ④ | check | need | **TRUOT** | Câu hỏi 'có điểm danh hả mn :v' không có ai trả lời, và không có tin nhắn nào nhắm vào nội dung câu hỏi này. D |
| GS-12 | `M67980` | ④ | check | check | dat | Câu hỏi chưa được giải đáp, có 2 tin nhắn trả lời nhưng không có thông tin rõ ràng từ người có thẩm quyền. Tin |
| GS-13 | `M30201` | hiem | need | need | dat | Câu hỏi về điểm chuyên cần chưa được trả lời bởi ai trong kênh, và không có ai nhắc đến câu hỏi này trong các  |
| GS-14 | `M36687` | hiem | check | need | **TRUOT** | Câu hỏi chưa được trả lời, chỉ có một tin nhắn không có nội dung trả lời cụ thể từ người khác. Không có ai trả |
| GS-15 | `M19124` | hiem | check | done | **TRUOT** | Câu hỏi đã được trả lời đầy đủ và đúng ý trong vòng 2 giờ từ một người dùng khác, không có mâu thuẫn nào với c |
| GS-16 | `M60122` | thuong | need | need | dat | Câu hỏi chưa được ai trả lời và không có ai nhắc đến nội dung câu hỏi trong các tin nhắn khác. Không có reply  |
| GS-17 | `M04392` | thuong | need | need | dat | Câu hỏi chưa được ai trả lời và không có phản hồi nào từ người dùng khác trong kênh. Cần chờ xem có ai trả lời |
| GS-18 | `M03948` | thuong | need | check | **TRUOT** | Câu hỏi chưa được trả lời và có tin nhắn sau đó từ người hỏi, nhưng không có ai trả lời trực tiếp cho câu hỏi  |
| GS-19 | `M17206` | thuong | need | need | dat | Câu hỏi chưa được giải đáp vì không có ai trả lời trong kênh. Không có tin nhắn nào nhắm vào nội dung câu hỏi. |
| GS-20 | `M18056` | thuong | need | done | **TRUOT** | Câu hỏi 'xem xp ở đâu' đã được trả lời đầy đủ trong tin nhắn của BOT với nội dung hướng dẫn cách theo dõi hoặc |
| GS-21 | `M83358` | thuong | done | done | dat | Câu hỏi đã được trả lời đầy đủ trong vòng 2 giờ từ người dùng khác (D3694) với thông tin chính xác về số lượng |
| GS-22 | `M15562` | thuong | done | check | **TRUOT** | Câu hỏi về việc hợp tác giữa hai team đã nhận được một số phản hồi từ người khác, nhưng chưa có câu trả lời rõ |
| GS-23 | `M20982` | thuong | done | check | **TRUOT** | Câu hỏi chưa được giải đáp và không có ai trả lời trực tiếp. Tuy nhiên, có một số tin nhắn trong cùng kênh như |
| GS-24 | `M49586` | thuong | done | need | **TRUOT** | Câu hỏi không có nội dung cụ thể để giải đáp và không có ai trả lời, chỉ có một tin nhắn sau đó không liên qua |
| GS-25 | `M83711` | thuong | done | done | dat | Câu hỏi đã được trả lời đầy đủ bởi hai người khác nhau trong vòng 2 giờ. Tin nhắn đầu tiên đã hướng dẫn người  |

## 5. Phan tich case truot

**GS-02 · `M97637`** — ky vong `nogrounding`, AI tra ve `done`  
Nhom gan nhan vi: *Câu hỏi nhắc tới "file hay link" từ một cuộc trò chuyện không có trong kênh đã quét.*  
AI lap luan: *Câu hỏi đã được trả lời đầy đủ bởi BOT trong vòng 2 giờ, cung cấp thông tin chi tiết về file hướng dẫn mà người hỏi đang tìm kiếm.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-03/M97637.json`)_

**GS-03 · `M51326`** — ky vong `nogrounding`, AI tra ve `done`  
Nhom gan nhan vi: *Nội dung lỗi nằm trong 2 ảnh đính kèm, AI không đọc ảnh. Có người trả lời sau 11 giờ nhưng không kiểm được có đúng lỗi không.*  
AI lap luan: *Câu hỏi đã được trả lời đầy đủ và đúng ý trong vòng 2 giờ từ người dùng D6587. Tin trả lời cung cấp thông tin chi tiết về vấn đề mà người hỏi gặp phải và cách giải quyết.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-03/M51326.json`)_

**GS-05 · `M00553`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Chỉ được hẹn "mai hỏi luôn", chưa có câu trả lời thật.*  
AI lap luan: *Câu hỏi chưa được giải đáp vì chỉ có một tin nhắn hẹn hỏi lại mà không có câu trả lời cụ thể nào cho câu hỏi. Không có ai trả lời trực tiếp cho câu hỏi này.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-03/M00553.json`)_

**GS-06 · `M54679`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Có phản hồi nhưng né câu hỏi; chưa đủ 4 giờ quan sát trước khi dữ liệu kết thúc.*  
AI lap luan: *Câu hỏi chưa được ai trả lời, và không có ai nhắc đến nội dung câu hỏi trong các tin nhắn gần đây.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-03/M54679.json`)_

**GS-09 · `M88027`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Đã được chỉ chỗ gửi ticket sau 13 phút, nhưng chưa rõ yêu cầu gia hạn đã được xử lý chưa.*  
AI lap luan: *Câu hỏi chưa được giải đáp vì không có ai trả lời trực tiếp cho câu hỏi này. Các tin nhắn trong kênh không liên quan trực tiếp đến câu hỏi về việc gia hạn thời gian nộp Lab2.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-03/M88027.json`)_

**GS-10 · `M72484`** — ky vong `need`, AI tra ve `check`  
Nhom gan nhan vi: *Hỏi hạn nộp trong kênh bot nhưng không tag bot, không ai trả lời.*  
AI lap luan: *Câu hỏi về hạn nộp Lab02 chưa được giải đáp rõ ràng. Có nhiều tin nhắn liên quan đến việc nộp lab muộn nhưng không có thông tin cụ thể về hạn nộp. Câu hỏi vẫn đang trong quá trình thảo luận và chưa có câu trả lời chính thức từ người quản lý.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-03/M72484.json`)_

**GS-11 · `M18676`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Hai bạn học trả lời mâu thuẫn nhau về điểm danh workshop trong cùng buổi sáng.*  
AI lap luan: *Câu hỏi 'có điểm danh hả mn :v' không có ai trả lời, và không có tin nhắn nào nhắm vào nội dung câu hỏi này. Do đó, cần thêm thời gian để xem có ai trả lời hay không.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-03/M18676.json`)_

**GS-14 · `M36687`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Có trả lời, nhưng sau gần 12 giờ và qua câu hỏi "ké" của người khác.*  
AI lap luan: *Câu hỏi chưa được trả lời, chỉ có một tin nhắn không có nội dung trả lời cụ thể từ người khác. Không có ai trả lời trực tiếp cho câu hỏi này.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-03/M36687.json`)_

**GS-15 · `M19124`** — ky vong `check`, AI tra ve `done`  
Nhom gan nhan vi: *Có trả lời, nhưng sau 8 giờ.*  
AI lap luan: *Câu hỏi đã được trả lời đầy đủ và đúng ý trong vòng 2 giờ từ một người dùng khác, không có mâu thuẫn nào với các tin nhắn khác.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-03/M19124.json`)_

**GS-18 · `M03948`** — ky vong `need`, AI tra ve `check`  
Nhom gan nhan vi: *Hỏi trong kênh bot nhưng không tag bot, không ai trả lời.*  
AI lap luan: *Câu hỏi chưa được trả lời và có tin nhắn sau đó từ người hỏi, nhưng không có ai trả lời trực tiếp cho câu hỏi này. Câu hỏi vẫn còn đang chờ phản hồi từ người khác.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-03/M03948.json`)_

**GS-20 · `M18056`** — ky vong `need`, AI tra ve `done`  
Nhom gan nhan vi: *2 người hỏi cách xem XP trong cùng buổi chiều, không ai trả lời.*  
AI lap luan: *Câu hỏi 'xem xp ở đâu' đã được trả lời đầy đủ trong tin nhắn của BOT với nội dung hướng dẫn cách theo dõi hoặc tìm kiếm điểm XP. Tin nhắn này được gửi trong vòng 2 giờ sau khi câu hỏi được đặt ra.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-03/M18056.json`)_

**GS-22 · `M15562`** — ky vong `done`, AI tra ve `check`  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M45489)*  
AI lap luan: *Câu hỏi về việc hợp tác giữa hai team đã nhận được một số phản hồi từ người khác, nhưng chưa có câu trả lời rõ ràng và đầy đủ. Có một số ý kiến nhưng chưa có sự đồng thuận hay giải đáp cụ thể cho câu hỏi ban đầu.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-03/M15562.json`)_

**GS-23 · `M20982`** — ky vong `done`, AI tra ve `check`  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M92726)*  
AI lap luan: *Câu hỏi chưa được giải đáp và không có ai trả lời trực tiếp. Tuy nhiên, có một số tin nhắn trong cùng kênh nhưng không liên quan đến câu hỏi này. Câu hỏi vẫn còn đang chờ phản hồi từ người khác.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-03/M20982.json`)_

**GS-24 · `M49586`** — ky vong `done`, AI tra ve `need`  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M17083)*  
AI lap luan: *Câu hỏi không có nội dung cụ thể để giải đáp và không có ai trả lời, chỉ có một tin nhắn sau đó không liên quan đến câu hỏi.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-03/M49586.json`)_


## 6. Doi chieu quality bar

Quality bar (chot tai CP4, xem `spec.md` §7): bo sot <=1/20 cau that su bo ngo (recall >=95%),
bao thua <=30%, va 0 muc lo ten nguoi.

- Recall luot nay: **88.2%** — CHUA DAT
- Bao thua: **12.0%** — DAT
- Lo ten nguoi: **0** — ban tin chi xuat `msg_id` va link, khong xuat tac gia
