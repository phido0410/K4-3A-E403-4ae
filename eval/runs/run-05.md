# Ket qua chay golden set — luot `run-05`

- **Model:** `gpt-4o-mini` · prompt `v5`
- **Luc chay:** 17/09/2026 09:32
- **Bo test:** `eval/golden_set.json` — 25 case
- **Ground truth:** `codebase/labels.js` (nhom doc tay 142 tin)
- **Log tung case:** `eval/logs/run-05/`

## 1. Tong hop

| Chi so | So |
|---|---|
| Tong case | 25 |
| Dat | 14 |
| Truot | 11 |
| **Ty le dat** | **56.0%** |
| Bo sot cau con ton (xep nham thanh `done`) | **2/17** |
| Recall tren nhom can TA xem | **88.2%** |
| Bao thua (`done` bi xep thanh can xem) | 2 |

> Ty le dat chung khong phai chi so quan trong nhat. Bo sot dat hon bao thua nhieu lan:
> bao thua ton cua TA 10 giay, bo sot thi hoc vien bi bo roi ma khong ai biet.

## 2. Ket qua theo lop cho kho

| Lop | Case | Dat | Ty le |
|---|---|---|---|
| ① Nguon su that | 3 | 0 | 0% |
| ② Mo ho / thieu thong tin | 3 | 3 | 100% |
| ③ Ngoai pham vi / tham quyen | 3 | 3 | 100% |
| ④ Dac thu domain | 3 | 2 | 67% |
| Case thuong | 10 | 6 | 60% |
| Case hiem | 4 | 0 | 0% |

## 3. Ma tran nham lan

| ky vong \ AI tra ve | need | check | nogrounding | done |
|---|---|---|---|---|
| **need** | 6 | 3 | · | 1 |
| **check** | 1 | 5 | · | 1 |
| **nogrounding** | 1 | 1 | · | 1 |
| **done** | 1 | 1 | · | 3 |

## 4. Tung case

| Case | Tin | Lop | Ky vong | AI tra ve | Dat | Ly do AI dua ra |
|---|---|---|---|---|---|---|
| GS-01 | `M80884` | ① | nogrounding | need | **TRUOT** | Câu hỏi không có ai trả lời, chỉ là nhắc nhở một người khác trả lời tin nhắn trước đó. |
| GS-02 | `M97637` | ① | nogrounding | done | **TRUOT** | Câu hỏi đã được giải đáp đầy đủ trong tin nhắn M08439 từ BOT, chỉ sau 1 phút kể từ khi hỏi. Không có mâu thuẫn |
| GS-03 | `M51326` | ① | nogrounding | check | **TRUOT** | Câu hỏi có nội dung rõ ràng và có một phản hồi trực tiếp từ một người dùng khác, tuy nhiên phản hồi đó không h |
| GS-04 | `M33885` | ② | need | need | dat | Câu hỏi chưa được giải đáp vì không có ai trả lời cho câu hỏi này trong khoảng thời gian 30 phút trước và sau  |
| GS-05 | `M00553` | ② | check | check | dat | Câu hỏi chưa được giải đáp, có một tin nhắn trực tiếp từ người khác nhắc đến câu hỏi này, nhưng chưa có câu tr |
| GS-06 | `M54679` | ② | check | check | dat | Câu hỏi về thời gian demo và QnA chưa được trả lời. Có một số tin nhắn liên quan nhưng không có ai trả lời trự |
| GS-07 | `M30246` | ③ | need | need | dat | Câu hỏi chưa được giải đáp vì không có ai trả lời cho câu hỏi này trong khoảng thời gian 30 phút sau khi hỏi. |
| GS-08 | `M27566` | ③ | need | need | dat | Câu hỏi chưa được giải đáp vì không có ai trả lời cho câu hỏi này trong khoảng thời gian 30 phút sau khi hỏi. |
| GS-09 | `M88027` | ③ | check | check | dat | Câu hỏi chưa được trả lời rõ ràng và có một số tin nhắn liên quan nhưng không có câu trả lời cụ thể cho câu hỏ |
| GS-10 | `M72484` | ④ | need | check | **TRUOT** | Câu hỏi 'Hạn nộp Lab02' chưa được giải đáp rõ ràng trong các tin nhắn trước đó. Tin nhắn từ BOT chỉ hướng dẫn  |
| GS-11 | `M18676` | ④ | check | check | dat | Câu hỏi 'có điểm danh hả mn :v' có liên quan đến nội dung trước đó, cụ thể là câu hỏi 'mình điểm danh ws ko ạ' |
| GS-12 | `M67980` | ④ | check | check | dat | Buoc 1: Cau hoi khong co trỏ tới thu gi ma ngu canh khong chua. Buoc 2: Co nguoi dung toi cau hoi, vi co tin t |
| GS-13 | `M30201` | hiem | need | check | **TRUOT** | Câu hỏi về điểm chuyên cần chưa được trả lời rõ ràng. Có một tin nhắn trả lời nhưng không cung cấp thông tin c |
| GS-14 | `M36687` | hiem | check | need | **TRUOT** | Câu hỏi chưa được giải đáp vì không có ai trả lời cho câu hỏi này, chỉ có một tin nhắc đến việc 'em ké câu hỏi |
| GS-15 | `M19124` | hiem | check | done | **TRUOT** | Câu hỏi đã được trả lời đầy đủ và đúng ý trong vòng 2 giờ bởi một người dùng khác, không có mâu thuẫn nào với  |
| GS-16 | `M60122` | thuong | need | need | dat | Câu hỏi chưa được giải đáp vì không có ai trả lời cho câu hỏi này trong khoảng thời gian 30 phút trước và sau. |
| GS-17 | `M04392` | thuong | need | need | dat | Câu hỏi chưa được giải đáp vì không có ai trả lời cho câu hỏi này trong khoảng thời gian 30 phút sau khi hỏi. |
| GS-18 | `M03948` | thuong | need | check | **TRUOT** | Câu hỏi chưa được giải đáp và có tin nhắn từ người hỏi sau đó, nhưng không có ai trả lời cho câu hỏi này. Câu  |
| GS-19 | `M17206` | thuong | need | need | dat | Câu hỏi chưa được giải đáp vì không có ai trả lời cho câu hỏi này trong khoảng thời gian 30 phút sau khi hỏi. |
| GS-20 | `M18056` | thuong | need | done | **TRUOT** | Câu hỏi 'xem xp ở đâu' đã được trả lời bởi BOT trước đó trong tin M42137 và M45780. Câu trả lời rõ ràng và đầy |
| GS-21 | `M83358` | thuong | done | done | dat | Câu hỏi đã được trả lời đầy đủ trong vòng 2 giờ bởi người dùng khác (D3694) với nội dung cụ thể về số lượng th |
| GS-22 | `M15562` | thuong | done | done | dat | Câu hỏi đã được trả lời đầy đủ bởi người dùng D3694 trong tin nhắn M45489, không có mâu thuẫn nào và nằm trong |
| GS-23 | `M20982` | thuong | done | check | **TRUOT** | Câu hỏi của học viên về việc điền hồ sơ năng lực có thể bị xem xét kết thúc đào tạo sớm hay không chưa được gi |
| GS-24 | `M49586` | thuong | done | need | **TRUOT** | Câu hỏi không có nội dung cụ thể và không có ai trả lời cho câu hỏi này, chỉ có các tin nhắn liên quan đến câu |
| GS-25 | `M83711` | thuong | done | done | dat | Câu hỏi đã được trả lời đầy đủ trong vòng 2 giờ bởi người dùng khác (D6604) với nội dung xác nhận bài mới đã đ |

## 5. Phan tich case truot

**GS-01 · `M80884`** — ky vong `nogrounding`, AI tra ve `need`  ·  nguyen nhan nhom **C**  
Nhom gan nhan vi: *Học viên nhờ admin trả lời tin nhắn riêng. Hệ thống không đọc tin nhắn riêng nên không biết đã được xử lý chưa.*  
AI lap luan: *Câu hỏi không có ai trả lời, chỉ là nhắc nhở một người khác trả lời tin nhắn trước đó.*  
**Chan doan:** Cau hoi la 'rep tin nhan e voi a' — can cu nam trong tin nhan rieng, ngoai tam quan sat. Model mo ta dung ('chi la nhac nho mot nguoi khac tra loi') nhung van chon need. Buoc 1 chua du manh voi cau hoi tro ra ngoai Discord.  
**Huong xu ly:** Them vi du 'nho rep tin nhan rieng' vao buoc 1 cua prompt.  

**GS-02 · `M97637`** — ky vong `nogrounding`, AI tra ve `done`  ·  nguyen nhan nhom **C**  
Nhom gan nhan vi: *Câu hỏi nhắc tới "file hay link" từ một cuộc trò chuyện không có trong kênh đã quét.*  
AI lap luan: *Câu hỏi đã được giải đáp đầy đủ trong tin nhắn M08439 từ BOT, chỉ sau 1 phút kể từ khi hỏi. Không có mâu thuẫn nào với các tin nhắn khác.*  
**Chan doan:** BOT tra loi sau 1 phut nen model ket luan done, bo qua viec cau hoi nhac toi 'file hay link' tu mot cuoc tro chuyen khong co trong ngu canh.  
**Huong xu ly:** Buoc 1 phai chay truoc va doc lap voi viec co hay khong co tin tra loi gan.  

**GS-03 · `M51326`** — ky vong `nogrounding`, AI tra ve `check`  ·  nguyen nhan nhom **C**  
Nhom gan nhan vi: *Nội dung lỗi nằm trong 2 ảnh đính kèm, AI không đọc ảnh. Có người trả lời sau 11 giờ nhưng không kiểm được có đúng lỗi không.*  
AI lap luan: *Câu hỏi có nội dung rõ ràng và có một phản hồi trực tiếp từ một người dùng khác, tuy nhiên phản hồi đó không hoàn toàn giải quyết vấn đề mà người hỏi đang gặp phải. Cần kiểm tra thêm để xác định xem có ai khác trả lời hay không.*  
**Chan doan:** Ngu canh CO co 'co_anh_dinh_kem: true' nhung model khong dung no de kich hoat nogrounding. Luot 5 da tien tu done sang check, van chua dung.  
**Huong xu ly:** Chuyen co anh dinh kem thanh luat cung trong code thay vi de model tu quyet.  

**GS-10 · `M72484`** — ky vong `need`, AI tra ve `check`  ·  nguyen nhan nhom **B**  
Nhom gan nhan vi: *Hỏi hạn nộp trong kênh bot nhưng không tag bot, không ai trả lời.*  
AI lap luan: *Câu hỏi 'Hạn nộp Lab02' chưa được giải đáp rõ ràng trong các tin nhắn trước đó. Tin nhắn từ BOT chỉ hướng dẫn kiểm tra các nguồn thông tin mà không cung cấp thông tin cụ thể về hạn nộp. Câu hỏi này có người dùng hỏi lại sau đó, cho thấy vẫn còn thắc mắc.*  
**Chan doan:** Cau hoi 'Han nop Lab02' trong kenh bot dong tin. Ngu canh day tin BOT tra loi nguoi khac ve deadline, model tuong da co huong dan.  
**Huong xu ly:** Loc ngu canh theo chu de, hoac giam cua so o kenh co mat do tin cao.  

**GS-13 · `M30201`** — ky vong `need`, AI tra ve `check`  ·  nguyen nhan nhom **A**  
Nhom gan nhan vi: *Có reply sau 3 phút nhưng reply nói về nhận role, không trả lời câu hỏi.*  
AI lap luan: *Câu hỏi về điểm chuyên cần chưa được trả lời rõ ràng. Có một tin nhắn trả lời nhưng không cung cấp thông tin cụ thể về câu hỏi. Cần kiểm tra thêm để xác định xem có ai khác trả lời hay không.*  
**Chan doan:** Co reply sau 3 phut nhung noi ve nhan role. Nhom coi lac de = khong ai dung toi = need; model coi co reply = check.  
**Huong xu ly:** Chot lai dinh nghia trong spec §7 truoc CP4: reply lac de tinh la need hay check.  

**GS-14 · `M36687`** — ky vong `check`, AI tra ve `need`  ·  nguyen nhan nhom **D**  
Nhom gan nhan vi: *Có trả lời, nhưng sau gần 12 giờ và qua câu hỏi "ké" của người khác.*  
AI lap luan: *Câu hỏi chưa được giải đáp vì không có ai trả lời cho câu hỏi này, chỉ có một tin nhắc đến việc 'em ké câu hỏi ạ' mà không có thông tin nào cụ thể về việc có group tập gym hay bơi.*  
**Chan doan:** Cau tra loi den sau 705 phut qua cau hoi 'ke' cua nguoi khac — nam ngoai moi cua so thoi gian hop ly.  
**Huong xu ly:** Khong sua bang prompt. Can tim kiem theo ngu nghia thay vi theo thoi gian; de lai sau CP3.  

**GS-15 · `M19124`** — ky vong `check`, AI tra ve `done`  ·  nguyen nhan nhom **E**  
Nhom gan nhan vi: *Có trả lời, nhưng sau 8 giờ.*  
AI lap luan: *Câu hỏi đã được trả lời đầy đủ và đúng ý trong vòng 2 giờ bởi một người dùng khác, không có mâu thuẫn nào với các tin nhắn khác.*  
**Chan doan:** Luot 5 da them sau_bao_phut = 487 vao reply truc tiep, nhung model van viet 'trong vong 2 gio'. Day la loi tuan thu, khong phai thieu du lieu.  
**Huong xu ly:** Tinh san co 'tra_loi_muon: true' trong code thay vi de model tu so sanh so.  

**GS-18 · `M03948`** — ky vong `need`, AI tra ve `check`  ·  nguyen nhan nhom **A**  
Nhom gan nhan vi: *Hỏi trong kênh bot nhưng không tag bot, không ai trả lời.*  
AI lap luan: *Câu hỏi chưa được giải đáp và có tin nhắn từ người hỏi sau đó, nhưng không có ai trả lời cho câu hỏi này. Câu hỏi có thể đã được nhắc lại trong tin sau đó, nhưng không có thông tin nào cho thấy đã có câu trả lời chính thức. Do đó, cần kiểm tra thêm.*  
**Chan doan:** Khong ai tra loi; chi co chinh nguoi hoi nhan lai. Model tinh viec do la 'co nguoi dung toi'.  
**Huong xu ly:** Noi ro trong prompt: tin cua chinh nguoi hoi khong tinh la co nguoi dung toi.  

**GS-20 · `M18056`** — ky vong `need`, AI tra ve `done`  ·  nguyen nhan nhom **F**  
Nhom gan nhan vi: *2 người hỏi cách xem XP trong cùng buổi chiều, không ai trả lời.*  
AI lap luan: *Câu hỏi 'xem xp ở đâu' đã được trả lời bởi BOT trước đó trong tin M42137 và M45780. Câu trả lời rõ ràng và đầy đủ, không có mâu thuẫn nào với các tin nhắn khác. Câu hỏi được đặt ra trong vòng 2 giờ sau khi có câu trả lời từ BOT.*  
**Chan doan:** Cau hoi giong het cua nguoi khac da duoc BOT tra loi 19 phut truoc trong cung kenh. Ca nhom va AI deu doc dung du lieu — khac nhau o dinh nghia san pham.  
**Huong xu ly:** Nhom phai chot truoc CP4: xep need, check, hay them trang thai 'da co dap an, chi can tro'.  

**GS-23 · `M20982`** — ky vong `done`, AI tra ve `check`  ·  nguyen nhan nhom **A**  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M92726)*  
AI lap luan: *Câu hỏi của học viên về việc điền hồ sơ năng lực có thể bị xem xét kết thúc đào tạo sớm hay không chưa được giải đáp. Không có ai trả lời trực tiếp cho câu hỏi này, nhưng có một số tin nhắn liên quan đến việc hỗ trợ thông tin. Cần kiểm tra thêm để xác định xem có ai trả lời trong vòng 120 phút hay không.*  
**Chan doan:** Co tra loi nhung model danh gia la chua du ro nen ha xuong check. Bang chung mong, ranh gioi done/check con mo.  
**Huong xu ly:** Bo sung tieu chi 'du de nguoi hoi di tiep' vao dinh nghia done.  

**GS-24 · `M49586`** — ky vong `done`, AI tra ve `need`  ·  nguyen nhan nhom **G**  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M17083)*  
AI lap luan: *Câu hỏi không có nội dung cụ thể và không có ai trả lời cho câu hỏi này, chỉ có các tin nhắn liên quan đến câu hỏi khác.*  
**Chan doan:** Tin la 'Kieu em ko co cau hoi nao hoi, co on ko a :))' — khong phai cau hoi can nguoi tra loi. Bon nhan hien tai khong co cho de xep.  
**Huong xu ly:** Them nhan thu nam 'khong phai cau hoi', hoac quy uoc xep vao done kem ly do.  

### Gom theo nhom nguyen nhan

| Nhom | So case | Mo ta |
|---|---|---|
| **A** | 3 | Ranh gioi need/check: nhom coi reply lac de hoac '+1' la KHONG ai dung toi (need); model coi co reply la da dung toi (check). |
| **B** | 1 | Ngu canh lan hoi thoai khac: kenh dong, cua so +/-30 phut chua day tin cua cuoc noi chuyen khac, model tuong do la cau tra loi. |
| **C** | 3 | nogrounding bi lan at: khi co bat ky tin tra loi nao o gan, model bo qua buoc 1 va khong con hoi 'can cu co nam trong tam quan sat khong'. |
| **D** | 1 | Cua so thoi gian: cau tra loi den ngoai +/-30 phut thi khong bao gio vao ngu canh. Day la gioi han thiet ke, khong sua duoc bang prompt. |
| **E** | 1 | Model doc sai du lieu da duoc cung cap (vi du bo qua truong sau_bao_phut). |
| **F** | 1 | Ranh gioi san pham chua dinh nghia: dap an da co san trong kenh cho cau hoi giong het cua nguoi khac. |
| **G** | 1 | Thieu nhan thu nam cho 'khong phai cau hoi can nguoi tra loi'. |


## 6. Doi chieu quality bar

Quality bar (chot tai CP4, xem `spec.md` §7): bo sot <=1/20 cau that su bo ngo (recall >=95%),
bao thua <=30%, va 0 muc lo ten nguoi.

- Recall luot nay: **88.2%** — CHUA DAT
- Bao thua: **8.0%** — DAT
- Lo ten nguoi: **0** — ban tin chi xuat `msg_id` va link, khong xuat tac gia
