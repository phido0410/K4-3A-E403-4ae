# Ket qua chay golden set — luot `run-01`

- **Model:** `gpt-4o-mini` · prompt `v1`
- **Luc chay:** 17/09/2026 11:03
- **Bo test:** `eval/golden_set.json` — 25 case
- **Ground truth:** `codebase/labels.js` (nhom doc tay 142 tin)
- **Log tung case:** `eval/logs/run-01/`

## 1. Tong hop

| Chi so | So |
|---|---|
| Tong case | 25 |
| Dat | 10 |
| Truot | 15 |
| **Ty le dat** | **40.0%** |
| Bo sot (case khong phai `done` ma AI xep `done`) | **4/20** |
| Recall tren 20 case can TA xem | **80.0%** |
| Muc xuat hien tren ban tin | 19 |
| Bao thua (`done` bi dua vao ban tin) | **3/19 = 15.8%** |

> Ty le dat chung khong phai chi so quan trong nhat. Bo sot dat hon bao thua nhieu lan:
> bao thua ton cua TA 10 giay, bo sot thi hoc vien bi bo roi ma khong ai biet.

## 2. Ket qua theo lop cho kho

| Lop | Case | Dat | Ty le |
|---|---|---|---|
| ① Nguon su that | 3 | 0 | 0% |
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
| **nogrounding** | 1 | · | · | 2 |
| **done** | 1 | 2 | · | 2 |

## 4. Tung case

| Case | Tin | Lop | Ky vong | AI tra ve | Dat | Ly do AI dua ra |
|---|---|---|---|---|---|---|
| GS-01 | `M80884` | ① | nogrounding | need | **TRUOT** | Câu hỏi không nhận được phản hồi nào từ người khác, chỉ có một tin nhắn không liên quan. Do đó, không thể kết  |
| GS-02 | `M97637` | ① | nogrounding | done | **TRUOT** | Câu hỏi đã được trả lời đầy đủ bởi BOT với hướng dẫn chi tiết và các liên kết cần thiết để người hỏi có thể th |
| GS-03 | `M51326` | ① | nogrounding | done | **TRUOT** | Câu hỏi đã được trả lời đầy đủ với thông tin chi tiết về lỗi và cách khắc phục. Người hỏi có thể tiếp tục với  |
| GS-04 | `M33885` | ② | need | need | dat | Câu hỏi về việc bị out ra không có ai trả lời, và không có thông tin nào trong các tin nhắn khác liên quan đến |
| GS-05 | `M00553` | ② | check | need | **TRUOT** | Câu hỏi chưa được trả lời cụ thể, chỉ có một phản hồi không rõ ràng từ người khác mà không cung cấp thông tin  |
| GS-06 | `M54679` | ② | check | need | **TRUOT** | Không có ai trả lời trực tiếp cho câu hỏi về thời gian demo và QnA, chỉ có một phản hồi không rõ ràng từ người |
| GS-07 | `M30246` | ③ | need | need | dat | Không có ai trả lời câu hỏi của học viên, và không có thông tin nào trong tin cùng kênh trong 30 phút để xác n |
| GS-08 | `M27566` | ③ | need | need | dat | Không có ai trả lời câu hỏi về việc cấp giấy chứng nhận sinh viên, và tin nhắn trong cùng kênh không liên quan |
| GS-09 | `M88027` | ③ | check | need | **TRUOT** | Câu hỏi về việc gia hạn thời gian nộp bài chưa được trả lời cụ thể. Các phản hồi từ học viên không cung cấp th |
| GS-10 | `M72484` | ④ | need | check | **TRUOT** | Câu hỏi về hạn nộp Lab02 chưa được trả lời cụ thể. BOT đã cung cấp thông tin về cách tìm kiếm nhưng không đưa  |
| GS-11 | `M18676` | ④ | check | need | **TRUOT** | Câu hỏi 'có điểm danh hả mn :v' chưa được trả lời bởi ai trong kênh, và không có phản hồi nào liên quan đến câ |
| GS-12 | `M67980` | ④ | check | check | dat | Có hai phản hồi từ người khác, nhưng không rõ ràng về việc có ai đó đã trả lời câu hỏi chính xác hay không. Ph |
| GS-13 | `M30201` | hiem | need | need | dat | Câu hỏi về điểm chuyên cần chưa được trả lời bởi ai trong kênh, và không có thông tin nào cho thấy câu hỏi đã  |
| GS-14 | `M36687` | hiem | check | need | **TRUOT** | Câu hỏi chưa được trả lời, chỉ có một phản hồi không liên quan đến nội dung câu hỏi. |
| GS-15 | `M19124` | hiem | check | done | **TRUOT** | Câu hỏi đã được trả lời đầy đủ và rõ ràng về lý do deadline ghép đội tự do kết thúc sớm, đồng thời cung cấp th |
| GS-16 | `M60122` | thuong | need | need | dat | Câu hỏi về daily-standup chưa được trả lời, không có phản hồi nào từ người khác trong kênh. Các tin nhắn khác  |
| GS-17 | `M04392` | thuong | need | need | dat | Không có ai trả lời câu hỏi của người hỏi, và không có thông tin nào trong tin nhắn sau đó để xác nhận câu hỏi |
| GS-18 | `M03948` | thuong | need | check | **TRUOT** | Câu hỏi của học viên về việc không thấy lịch sử bên activity khi commit có thể đã được trả lời một phần bởi BO |
| GS-19 | `M17206` | thuong | need | need | dat | Câu hỏi chưa được giải đáp vì không có phản hồi nào từ người khác trong kênh. Không có thông tin nào cho thấy  |
| GS-20 | `M18056` | thuong | need | done | **TRUOT** | Câu hỏi 'xem xp ở đâu' đã được trả lời trong tin nhắn của BOT, cung cấp thông tin rõ ràng về cách theo dõi hoặ |
| GS-21 | `M83358` | thuong | done | done | dat | Câu hỏi đã được trả lời đầy đủ với thông tin chính xác về số lượng thành viên trong team. |
| GS-22 | `M15562` | thuong | done | check | **TRUOT** | Câu hỏi về việc hợp tác giữa hai team non-tech chưa được trả lời trực tiếp. Có một số phản hồi liên quan nhưng |
| GS-23 | `M20982` | thuong | done | need | **TRUOT** | Câu hỏi về việc điền hồ sơ năng lực và khả năng bị xem xét kết thúc đào tạo sớm chưa được trả lời. Không có ph |
| GS-24 | `M49586` | thuong | done | done | dat | Câu hỏi không yêu cầu thông tin cụ thể và không cần được trả lời. Người hỏi đã xác nhận không có câu hỏi nào v |
| GS-25 | `M83711` | thuong | done | check | **TRUOT** | Có hai phản hồi liên quan đến câu hỏi, nhưng không rõ ràng liệu câu hỏi đã được giải đáp hoàn toàn hay chưa. P |

### Case bi bo sot — loai loi dat nhat

| Case | Tin | Ky vong | AI tra ve |
|---|---|---|---|
| GS-02 | `M97637` | nogrounding | done |
| GS-03 | `M51326` | nogrounding | done |
| GS-15 | `M19124` | check | done |
| GS-20 | `M18056` | need | done |


## 5. Phan tich case truot

**GS-01 · `M80884`** — ky vong `nogrounding`, AI tra ve `need`  ·  nguyen nhan nhom **C**  
Nhom gan nhan vi: *Học viên nhờ admin trả lời tin nhắn riêng. Hệ thống không đọc tin nhắn riêng nên không biết đã được xử lý chưa.*  
AI lap luan: *Câu hỏi không nhận được phản hồi nào từ người khác, chỉ có một tin nhắn không liên quan. Do đó, không thể kết luận câu hỏi đã được giải đáp hay chưa.*  
**Chan doan:** Cau hoi la 'rep tin nhan e voi a' — can cu nam trong tin nhan rieng, ngoai tam quan sat. Model mo ta dung ('chi la nhac nho mot nguoi khac tra loi') nhung van chon need. Buoc 1 chua du manh voi cau hoi tro ra ngoai Discord.  
**Huong xu ly:** Them vi du 'nho rep tin nhan rieng' vao buoc 1 cua prompt.  

**GS-02 · `M97637`** — ky vong `nogrounding`, AI tra ve `done`  ·  nguyen nhan nhom **C**  
Nhom gan nhan vi: *Câu hỏi nhắc tới "file hay link" từ một cuộc trò chuyện không có trong kênh đã quét.*  
AI lap luan: *Câu hỏi đã được trả lời đầy đủ bởi BOT với hướng dẫn chi tiết và các liên kết cần thiết để người hỏi có thể thực hiện theo. Nội dung trả lời phù hợp với câu hỏi và cung cấp thông tin cần thiết.*  
**Chan doan:** BOT tra loi sau 1 phut nen model ket luan done, bo qua viec cau hoi nhac toi 'file hay link' tu mot cuoc tro chuyen khong co trong ngu canh.  
**Huong xu ly:** Buoc 1 phai chay truoc va doc lap voi viec co hay khong co tin tra loi gan.  

**GS-03 · `M51326`** — ky vong `nogrounding`, AI tra ve `done`  ·  nguyen nhan nhom **C**  
Nhom gan nhan vi: *Nội dung lỗi nằm trong 2 ảnh đính kèm, AI không đọc ảnh. Có người trả lời sau 11 giờ nhưng không kiểm được có đúng lỗi không.*  
AI lap luan: *Câu hỏi đã được trả lời đầy đủ với thông tin chi tiết về lỗi và cách khắc phục. Người hỏi có thể tiếp tục với câu hỏi khác.*  
**Chan doan:** Ngu canh CO co 'co_anh_dinh_kem: true' nhung model khong dung no de kich hoat nogrounding. Luot 5 da tien tu done sang check, van chua dung.  
**Huong xu ly:** Chuyen co anh dinh kem thanh luat cung trong code thay vi de model tu quyet.  

**GS-05 · `M00553`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Chỉ được hẹn "mai hỏi luôn", chưa có câu trả lời thật.*  
AI lap luan: *Câu hỏi chưa được trả lời cụ thể, chỉ có một phản hồi không rõ ràng từ người khác mà không cung cấp thông tin cần thiết để giải đáp câu hỏi. Không có ai trả lời trực tiếp về nội dung câu hỏi của học viên.*  
_Chua chan doan — doc log `eval/logs/run-01/M00553.json` roi bo sung vao eval/phan_tich.json_  

**GS-06 · `M54679`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Có phản hồi nhưng né câu hỏi; chưa đủ 4 giờ quan sát trước khi dữ liệu kết thúc.*  
AI lap luan: *Không có ai trả lời trực tiếp cho câu hỏi về thời gian demo và QnA, chỉ có một phản hồi không rõ ràng từ người khác. Cần thêm thông tin để xác định câu hỏi đã được giải đáp hay chưa.*  
_Chua chan doan — doc log `eval/logs/run-01/M54679.json` roi bo sung vao eval/phan_tich.json_  

**GS-09 · `M88027`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Đã được chỉ chỗ gửi ticket sau 13 phút, nhưng chưa rõ yêu cầu gia hạn đã được xử lý chưa.*  
AI lap luan: *Câu hỏi về việc gia hạn thời gian nộp bài chưa được trả lời cụ thể. Các phản hồi từ học viên không cung cấp thông tin rõ ràng về việc có thể gia hạn hay không, chỉ có một lời khuyên gửi ticket mà không có câu trả lời trực tiếp cho câu hỏi của người hỏi.*  
_Chua chan doan — doc log `eval/logs/run-01/M88027.json` roi bo sung vao eval/phan_tich.json_  

**GS-10 · `M72484`** — ky vong `need`, AI tra ve `check`  ·  nguyen nhan nhom **B**  
Nhom gan nhan vi: *Hỏi hạn nộp trong kênh bot nhưng không tag bot, không ai trả lời.*  
AI lap luan: *Câu hỏi về hạn nộp Lab02 chưa được trả lời cụ thể. BOT đã cung cấp thông tin về cách tìm kiếm nhưng không đưa ra ngày giờ cụ thể cho hạn nộp. Có một số phản hồi từ người khác nhưng không rõ ràng và không chính thức.*  
**Chan doan:** Cau hoi 'Han nop Lab02' trong kenh bot dong tin. Ngu canh day tin BOT tra loi nguoi khac ve deadline, model tuong da co huong dan.  
**Huong xu ly:** Loc ngu canh theo chu de, hoac giam cua so o kenh co mat do tin cao.  

**GS-11 · `M18676`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Hai bạn học trả lời mâu thuẫn nhau về điểm danh workshop trong cùng buổi sáng.*  
AI lap luan: *Câu hỏi 'có điểm danh hả mn :v' chưa được trả lời bởi ai trong kênh, và không có phản hồi nào liên quan đến câu hỏi này. Các tin nhắn khác không liên quan đến câu hỏi về điểm danh.*  
_Chua chan doan — doc log `eval/logs/run-01/M18676.json` roi bo sung vao eval/phan_tich.json_  

**GS-14 · `M36687`** — ky vong `check`, AI tra ve `need`  ·  nguyen nhan nhom **D**  
Nhom gan nhan vi: *Có trả lời, nhưng sau gần 12 giờ và qua câu hỏi "ké" của người khác.*  
AI lap luan: *Câu hỏi chưa được trả lời, chỉ có một phản hồi không liên quan đến nội dung câu hỏi.*  
**Chan doan:** Cau tra loi den sau 705 phut qua cau hoi 'ke' cua nguoi khac — nam ngoai moi cua so thoi gian hop ly.  
**Huong xu ly:** Khong sua bang prompt. Can tim kiem theo ngu nghia thay vi theo thoi gian; de lai sau CP3.  

**GS-15 · `M19124`** — ky vong `check`, AI tra ve `done`  ·  nguyen nhan nhom **E**  
Nhom gan nhan vi: *Có trả lời, nhưng sau 8 giờ.*  
AI lap luan: *Câu hỏi đã được trả lời đầy đủ và rõ ràng về lý do deadline ghép đội tự do kết thúc sớm, đồng thời cung cấp thông tin hỗ trợ từ BTC.*  
**Chan doan:** Luot 5 da them sau_bao_phut = 487 vao reply truc tiep, nhung model van viet 'trong vong 2 gio'. Day la loi tuan thu, khong phai thieu du lieu.  
**Huong xu ly:** Tinh san co 'tra_loi_muon: true' trong code thay vi de model tu so sanh so.  

**GS-18 · `M03948`** — ky vong `need`, AI tra ve `check`  ·  nguyen nhan nhom **A**  
Nhom gan nhan vi: *Hỏi trong kênh bot nhưng không tag bot, không ai trả lời.*  
AI lap luan: *Câu hỏi của học viên về việc không thấy lịch sử bên activity khi commit có thể đã được trả lời một phần bởi BOT, nhưng câu trả lời không trực tiếp giải thích lý do tại sao không thấy lịch sử đó. Học viên đã nhắc lại câu hỏi, cho thấy họ vẫn chưa nhận được câu trả lời thỏa đáng. Cần thêm thông tin để xác định rõ ràng.*  
**Chan doan:** Khong ai tra loi; chi co chinh nguoi hoi nhan lai. Model tinh viec do la 'co nguoi dung toi'.  
**Huong xu ly:** Noi ro trong prompt: tin cua chinh nguoi hoi khong tinh la co nguoi dung toi.  

**GS-20 · `M18056`** — ky vong `need`, AI tra ve `done`  ·  nguyen nhan nhom **F**  
Nhom gan nhan vi: *2 người hỏi cách xem XP trong cùng buổi chiều, không ai trả lời.*  
AI lap luan: *Câu hỏi 'xem xp ở đâu' đã được trả lời trong tin nhắn của BOT, cung cấp thông tin rõ ràng về cách theo dõi hoặc tìm kiếm điểm XP.*  
**Chan doan:** Cau hoi giong het cua nguoi khac da duoc BOT tra loi 19 phut truoc trong cung kenh. Ca nhom va AI deu doc dung du lieu — khac nhau o dinh nghia san pham.  
**Huong xu ly:** Nhom phai chot truoc CP4: xep need, check, hay them trang thai 'da co dap an, chi can tro'.  

**GS-22 · `M15562`** — ky vong `done`, AI tra ve `check`  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M45489)*  
AI lap luan: *Câu hỏi về việc hợp tác giữa hai team non-tech chưa được trả lời trực tiếp. Có một số phản hồi liên quan nhưng không rõ ràng về việc có thể bắt tay làm project hay không. Cần thêm thông tin từ các thành viên khác để có kết luận chính xác.*  
_Chua chan doan — doc log `eval/logs/run-01/M15562.json` roi bo sung vao eval/phan_tich.json_  

**GS-23 · `M20982`** — ky vong `done`, AI tra ve `need`  ·  nguyen nhan nhom **A**  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M92726)*  
AI lap luan: *Câu hỏi về việc điền hồ sơ năng lực và khả năng bị xem xét kết thúc đào tạo sớm chưa được trả lời. Không có phản hồi nào liên quan đến câu hỏi này trong các tin nhắn trong kênh. Các tin nhắn khác không liên quan đến câu hỏi cụ thể của người hỏi.*  
**Chan doan:** Co tra loi nhung model danh gia la chua du ro nen ha xuong check. Bang chung mong, ranh gioi done/check con mo.  
**Huong xu ly:** Bo sung tieu chi 'du de nguoi hoi di tiep' vao dinh nghia done.  

**GS-25 · `M83711`** — ky vong `done`, AI tra ve `check`  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M81490)*  
AI lap luan: *Có hai phản hồi liên quan đến câu hỏi, nhưng không rõ ràng liệu câu hỏi đã được giải đáp hoàn toàn hay chưa. Phản hồi đầu tiên chỉ hướng dẫn hỏi labcoach, trong khi phản hồi thứ hai xác nhận bài mới đã được up. Tuy nhiên, không có thông tin cụ thể về việc vlearn đã up bài mới hay chưa, nên không thể kết luận chắc chắn.*  
_Chua chan doan — doc log `eval/logs/run-01/M83711.json` roi bo sung vao eval/phan_tich.json_  

### Gom theo nhom nguyen nhan

| Nhom | So case | Mo ta |
|---|---|---|
| **A** | 2 | Ranh gioi need/check: nhom coi reply lac de hoac '+1' la KHONG ai dung toi (need); model coi co reply la da dung toi (check). |
| **B** | 1 | Ngu canh lan hoi thoai khac: kenh dong, cua so +/-30 phut chua day tin cua cuoc noi chuyen khac, model tuong do la cau tra loi. |
| **C** | 3 | nogrounding bi lan at: khi co bat ky tin tra loi nao o gan, model bo qua buoc 1 va khong con hoi 'can cu co nam trong tam quan sat khong'. |
| **D** | 1 | Cua so thoi gian: cau tra loi den ngoai +/-30 phut thi khong bao gio vao ngu canh. Day la gioi han thiet ke, khong sua duoc bang prompt. |
| **E** | 1 | Model doc sai du lieu da duoc cung cap (vi du bo qua truong sau_bao_phut). |
| **F** | 1 | Ranh gioi san pham chua dinh nghia: dap an da co san trong kenh cho cau hoi giong het cua nguoi khac. |


## 6. Doi chieu quality bar

Quality bar (chot tai CP4, xem `spec.md` §7): bo sot <=1/20 cau that su bo ngo (recall >=95%),
bao thua <=30%, va 0 muc lo ten nguoi.

- Recall luot nay: **80.0%** — CHUA DAT
- Bao thua: **15.8%** (3/19 muc tren ban tin) — DAT
- Lo ten nguoi: **0** — ban tin chi xuat `msg_id` va link, khong xuat tac gia
