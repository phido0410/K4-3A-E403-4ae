# Ket qua chay golden set — luot `run-04`

- **Model:** `gpt-4o-mini` · prompt `v4`
- **Luc chay:** 16/09/2026 23:47
- **Bo test:** `eval/golden_set.json` — 25 case
- **Ground truth:** `codebase/labels.js` (nhom doc tay 142 tin)
- **Log tung case:** `eval/logs/run-04/`

## 1. Tong hop

| Chi so | So |
|---|---|
| Tong case | 25 |
| Dat | 13 |
| Truot | 12 |
| **Ty le dat** | **52.0%** |
| Bo sot cau con ton (xep nham thanh `done`) | **2/17** |
| Recall tren nhom can TA xem | **88.2%** |
| Bao thua (`done` bi xep thanh can xem) | 3 |

> Ty le dat chung khong phai chi so quan trong nhat. Bo sot dat hon bao thua nhieu lan:
> bao thua ton cua TA 10 giay, bo sot thi hoc vien bi bo roi ma khong ai biet.

## 2. Ket qua theo lop cho kho

| Lop | Case | Dat | Ty le |
|---|---|---|---|
| ① Nguon su that | 3 | 1 | 33% |
| ② Mo ho / thieu thong tin | 3 | 2 | 67% |
| ③ Ngoai pham vi / tham quyen | 3 | 3 | 100% |
| ④ Dac thu domain | 3 | 2 | 67% |
| Case thuong | 10 | 5 | 50% |
| Case hiem | 4 | 0 | 0% |

## 3. Ma tran nham lan

| ky vong \ AI tra ve | need | check | nogrounding | done |
|---|---|---|---|---|
| **need** | 5 | 4 | · | 1 |
| **check** | 1 | 5 | · | 1 |
| **nogrounding** | · | · | 1 | 2 |
| **done** | · | 3 | · | 2 |

## 4. Tung case

| Case | Tin | Lop | Ky vong | AI tra ve | Dat | Ly do AI dua ra |
|---|---|---|---|---|---|---|
| GS-01 | `M80884` | ① | nogrounding | nogrounding | dat | Câu hỏi không có nội dung cụ thể mà chỉ nhắc đến việc trả lời tin nhắn của một người khác, không nằm trong ngữ |
| GS-02 | `M97637` | ① | nogrounding | done | **TRUOT** | Câu hỏi đã được giải đáp bởi BOT trong tin nhắn M08439, cung cấp hướng dẫn đầy đủ mà người hỏi cần. Thời gian  |
| GS-03 | `M51326` | ① | nogrounding | done | **TRUOT** | Câu hỏi đã được trả lời đầy đủ và đúng ý trong vòng 2 giờ bởi một người dùng khác, không có mâu thuẫn nào với  |
| GS-04 | `M33885` | ② | need | check | **TRUOT** | Câu hỏi 'vào mà cứ bị out ra thì phải làm sao ạ :v' không có ai trả lời trực tiếp, nhưng có một số tin nhắn tr |
| GS-05 | `M00553` | ② | check | check | dat | Câu hỏi chưa được giải đáp, có một tin nhắn trả lời trực tiếp từ người khác nhưng không cung cấp thông tin cụ  |
| GS-06 | `M54679` | ② | check | check | dat | Câu hỏi 'về thời gian demo + QnA thì sao vậy anh nhỉ ?' không có ai trả lời trực tiếp, nhưng có một số tin nhắ |
| GS-07 | `M30246` | ③ | need | need | dat | Câu hỏi của người hỏi chưa được ai trả lời, không có tin nhắn nào nhắm vào nội dung câu hỏi này trong khoảng t |
| GS-08 | `M27566` | ③ | need | need | dat | Câu hỏi chưa được giải đáp vì không có ai trả lời cho câu hỏi này trong khoảng thời gian 30 phút. Không có tin |
| GS-09 | `M88027` | ③ | check | check | dat | Buoc 1: Cau hoi khong co trỏ tới thu gi ma ngu canh khong chua. Buoc 2: Co nguoi dung toi cau hoi nay, vi co t |
| GS-10 | `M72484` | ④ | need | check | **TRUOT** | Câu hỏi 'Hạn nộp Lab02' chưa được giải đáp rõ ràng trong các tin nhắn trước đó. Tin nhắn từ BOT chỉ hướng dẫn  |
| GS-11 | `M18676` | ④ | check | check | dat | Câu hỏi 'có điểm danh hả mn :v' không có ai trả lời trực tiếp và không có thông tin nào từ tin nhắn trước đó h |
| GS-12 | `M67980` | ④ | check | check | dat | Câu hỏi có người dùng tới (tin M84013) nhưng chưa có câu trả lời chính thức. Cần kiểm tra thêm. |
| GS-13 | `M30201` | hiem | need | check | **TRUOT** | Câu hỏi chưa được trả lời và có một tin nhắn trả lời trực tiếp từ người khác nhưng không giải đáp câu hỏi. Cần |
| GS-14 | `M36687` | hiem | check | need | **TRUOT** | Câu hỏi chưa được ai trả lời và không có ai nhắc đến nội dung câu hỏi trong các tin nhắn trước đó. Chưa có thô |
| GS-15 | `M19124` | hiem | check | done | **TRUOT** | Câu hỏi đã được trả lời đầy đủ và đúng ý trong vòng 2 giờ bởi một người dùng khác, không có mâu thuẫn nào với  |
| GS-16 | `M60122` | thuong | need | need | dat | Câu hỏi chưa được giải đáp vì không có ai trả lời cho câu hỏi này trong khoảng thời gian 30 phút sau khi hỏi. |
| GS-17 | `M04392` | thuong | need | need | dat | Câu hỏi chưa được giải đáp vì không có ai trả lời cho câu hỏi này trong khoảng thời gian 30 phút sau khi hỏi. |
| GS-18 | `M03948` | thuong | need | check | **TRUOT** | Câu hỏi 'khi tôi commit tại sao ko thấy lịch sử bên activity ở kênh discord này' chưa được giải đáp. Có một ti |
| GS-19 | `M17206` | thuong | need | need | dat | Câu hỏi không có ai trả lời, không có tin nhắn nào nhắm vào nội dung câu hỏi này trong khoảng thời gian 30 phú |
| GS-20 | `M18056` | thuong | need | done | **TRUOT** | Câu hỏi 'xem xp ở đâu' đã được trả lời bởi BOT trước đó trong tin nhắn M42137 và M45780. Câu trả lời rõ ràng v |
| GS-21 | `M83358` | thuong | done | done | dat | Câu hỏi đã được trả lời đầy đủ trong vòng 2 giờ bởi người dùng khác (D3694) với nội dung rõ ràng. Không có mâu |
| GS-22 | `M15562` | thuong | done | check | **TRUOT** | Câu hỏi của học viên về việc hợp tác giữa hai team đã có một số phản hồi từ người khác, nhưng chưa có câu trả  |
| GS-23 | `M20982` | thuong | done | check | **TRUOT** | Câu hỏi của học viên về việc điền hồ sơ năng lực có thể bị xem xét kết thúc đào tạo sớm chưa được trả lời. Có  |
| GS-24 | `M49586` | thuong | done | check | **TRUOT** | Câu hỏi không có ai trả lời trực tiếp và không có thông tin nào cho thấy đã có câu trả lời chính thức. Tuy nhi |
| GS-25 | `M83711` | thuong | done | done | dat | Câu hỏi đã được trả lời đầy đủ trong vòng 2 giờ bởi người dùng khác (D6604) với thông tin rõ ràng về bài học m |

## 5. Phan tich case truot

**GS-02 · `M97637`** — ky vong `nogrounding`, AI tra ve `done`  
Nhom gan nhan vi: *Câu hỏi nhắc tới "file hay link" từ một cuộc trò chuyện không có trong kênh đã quét.*  
AI lap luan: *Câu hỏi đã được giải đáp bởi BOT trong tin nhắn M08439, cung cấp hướng dẫn đầy đủ mà người hỏi cần. Thời gian giữa câu hỏi và câu trả lời là 1 phút, không có mâu thuẫn nào với các tin nhắn khác.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-04/M97637.json`)_

**GS-03 · `M51326`** — ky vong `nogrounding`, AI tra ve `done`  
Nhom gan nhan vi: *Nội dung lỗi nằm trong 2 ảnh đính kèm, AI không đọc ảnh. Có người trả lời sau 11 giờ nhưng không kiểm được có đúng lỗi không.*  
AI lap luan: *Câu hỏi đã được trả lời đầy đủ và đúng ý trong vòng 2 giờ bởi một người dùng khác, không có mâu thuẫn nào với các tin nhắn khác.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-04/M51326.json`)_

**GS-04 · `M33885`** — ky vong `need`, AI tra ve `check`  
Nhom gan nhan vi: *Không ai phản hồi. Câu hỏi thiếu ngữ cảnh ("vào" hệ thống nào) — TA nên hỏi lại học viên.*  
AI lap luan: *Câu hỏi 'vào mà cứ bị out ra thì phải làm sao ạ :v' không có ai trả lời trực tiếp, nhưng có một số tin nhắn trước đó liên quan đến việc vào ra, không có câu trả lời cụ thể cho câu hỏi này. Cần kiểm tra thêm để xác định xem có ai trả lời trong thời gian tới không.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-04/M33885.json`)_

**GS-10 · `M72484`** — ky vong `need`, AI tra ve `check`  
Nhom gan nhan vi: *Hỏi hạn nộp trong kênh bot nhưng không tag bot, không ai trả lời.*  
AI lap luan: *Câu hỏi 'Hạn nộp Lab02' chưa được giải đáp rõ ràng trong các tin nhắn trước đó. Tin nhắn từ BOT chỉ hướng dẫn kiểm tra các nguồn thông tin mà không cung cấp thông tin cụ thể về hạn nộp. Câu hỏi này có người dùng hỏi và chưa có câu trả lời thỏa đáng trong vòng 2 giờ.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-04/M72484.json`)_

**GS-13 · `M30201`** — ky vong `need`, AI tra ve `check`  
Nhom gan nhan vi: *Có reply sau 3 phút nhưng reply nói về nhận role, không trả lời câu hỏi.*  
AI lap luan: *Câu hỏi chưa được trả lời và có một tin nhắn trả lời trực tiếp từ người khác nhưng không giải đáp câu hỏi. Cần kiểm tra thêm để xác định có ai trả lời hay không.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-04/M30201.json`)_

**GS-14 · `M36687`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Có trả lời, nhưng sau gần 12 giờ và qua câu hỏi "ké" của người khác.*  
AI lap luan: *Câu hỏi chưa được ai trả lời và không có ai nhắc đến nội dung câu hỏi trong các tin nhắn trước đó. Chưa có thông tin nào từ người dùng khác liên quan đến câu hỏi này.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-04/M36687.json`)_

**GS-15 · `M19124`** — ky vong `check`, AI tra ve `done`  
Nhom gan nhan vi: *Có trả lời, nhưng sau 8 giờ.*  
AI lap luan: *Câu hỏi đã được trả lời đầy đủ và đúng ý trong vòng 2 giờ bởi một người dùng khác, không có mâu thuẫn nào với các tin nhắn khác.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-04/M19124.json`)_

**GS-18 · `M03948`** — ky vong `need`, AI tra ve `check`  
Nhom gan nhan vi: *Hỏi trong kênh bot nhưng không tag bot, không ai trả lời.*  
AI lap luan: *Câu hỏi 'khi tôi commit tại sao ko thấy lịch sử bên activity ở kênh discord này' chưa được giải đáp. Có một tin nhắn từ người hỏi sau đó nhưng không có ai trả lời cụ thể cho câu hỏi này. Câu hỏi này có người dùng tới vì có tin nhắn nhắc lại câu hỏi từ người hỏi. Cần kiểm tra thêm để xem có ai trả lời trong thời gian tới không.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-04/M03948.json`)_

**GS-20 · `M18056`** — ky vong `need`, AI tra ve `done`  
Nhom gan nhan vi: *2 người hỏi cách xem XP trong cùng buổi chiều, không ai trả lời.*  
AI lap luan: *Câu hỏi 'xem xp ở đâu' đã được trả lời bởi BOT trước đó trong tin nhắn M42137 và M45780. Câu trả lời rõ ràng và đầy đủ, không có mâu thuẫn nào với các tin nhắn khác. Thời gian hỏi và trả lời đều trong khoảng thời gian 2 giờ.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-04/M18056.json`)_

**GS-22 · `M15562`** — ky vong `done`, AI tra ve `check`  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M45489)*  
AI lap luan: *Câu hỏi của học viên về việc hợp tác giữa hai team đã có một số phản hồi từ người khác, nhưng chưa có câu trả lời rõ ràng và đầy đủ cho câu hỏi này. Câu hỏi được đặt ra vào lúc 21:32 và có phản hồi từ một người dùng khác vào lúc 21:32, nhưng không có câu trả lời chính thức nào từ người có thẩm quyền. Do đó, cần kiểm tra thêm.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-04/M15562.json`)_

**GS-23 · `M20982`** — ky vong `done`, AI tra ve `check`  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M92726)*  
AI lap luan: *Câu hỏi của học viên về việc điền hồ sơ năng lực có thể bị xem xét kết thúc đào tạo sớm chưa được trả lời. Có một tin nhắn từ người hỏi cảm ơn sau đó, nhưng không có câu trả lời cụ thể cho câu hỏi này. Do đó, cần kiểm tra thêm.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-04/M20982.json`)_

**GS-24 · `M49586`** — ky vong `done`, AI tra ve `check`  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M17083)*  
AI lap luan: *Câu hỏi không có ai trả lời trực tiếp và không có thông tin nào cho thấy đã có câu trả lời chính thức. Tuy nhiên, có một tin nhắn từ người khác nói rằng không có câu hỏi thì chỉ cần lắng nghe, điều này có thể được coi là một phản hồi liên quan. Cần kiểm tra thêm để xác định xem có ai khác trả lời hay không.*  
Huong xu ly: _(dien tay sau khi doc log `eval/logs/run-04/M49586.json`)_


## 6. Doi chieu quality bar

Quality bar (chot tai CP4, xem `spec.md` §7): bo sot <=1/20 cau that su bo ngo (recall >=95%),
bao thua <=30%, va 0 muc lo ten nguoi.

- Recall luot nay: **88.2%** — CHUA DAT
- Bao thua: **12.0%** — DAT
- Lo ten nguoi: **0** — ban tin chi xuat `msg_id` va link, khong xuat tac gia
