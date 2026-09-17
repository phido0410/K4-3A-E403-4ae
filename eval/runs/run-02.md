# Ket qua chay golden set — luot `run-02`

- **Model:** `gpt-4o-mini` · prompt `v2`
- **Luc chay:** 17/09/2026 09:32
- **Bo test:** `eval/golden_set.json` — 25 case
- **Ground truth:** `codebase/labels.js` (nhom doc tay 142 tin)
- **Log tung case:** `eval/logs/run-02/`

## 1. Tong hop

| Chi so | So |
|---|---|
| Tong case | 25 |
| Dat | 10 |
| Truot | 15 |
| **Ty le dat** | **40.0%** |
| Bo sot cau con ton (xep nham thanh `done`) | **2/17** |
| Recall tren nhom can TA xem | **88.2%** |
| Bao thua (`done` bi xep thanh can xem) | 4 |

> Ty le dat chung khong phai chi so quan trong nhat. Bo sot dat hon bao thua nhieu lan:
> bao thua ton cua TA 10 giay, bo sot thi hoc vien bi bo roi ma khong ai biet.

## 2. Ket qua theo lop cho kho

| Lop | Case | Dat | Ty le |
|---|---|---|---|
| ① Nguon su that | 3 | 2 | 67% |
| ② Mo ho / thieu thong tin | 3 | 1 | 33% |
| ③ Ngoai pham vi / tham quyen | 3 | 1 | 33% |
| ④ Dac thu domain | 3 | 1 | 33% |
| Case thuong | 10 | 4 | 40% |
| Case hiem | 4 | 2 | 50% |

## 3. Ma tran nham lan

| ky vong \ AI tra ve | need | check | nogrounding | done |
|---|---|---|---|---|
| **need** | 7 | · | 2 | 1 |
| **check** | 6 | · | · | 1 |
| **nogrounding** | · | · | 2 | 1 |
| **done** | 2 | 2 | · | 1 |

## 4. Tung case

| Case | Tin | Lop | Ky vong | AI tra ve | Dat | Ly do AI dua ra |
|---|---|---|---|---|---|---|
| GS-01 | `M80884` | ① | nogrounding | nogrounding | dat | Câu hỏi không rõ ràng vì nó yêu cầu một người cụ thể ([@D9617]) trả lời tin nhắn mà không có thông tin nào về  |
| GS-02 | `M97637` | ① | nogrounding | done | **TRUOT** | Câu hỏi đã được trả lời đầy đủ bởi BOT trong tin nhắn M08439, cung cấp thông tin chi tiết về quy trình và các  |
| GS-03 | `M51326` | ① | nogrounding | nogrounding | dat | Câu hỏi có nhắc đến lỗi cụ thể nhưng không có thông tin chi tiết về lỗi đó trong ngữ cảnh. Hơn nữa, có ảnh đín |
| GS-04 | `M33885` | ② | need | need | dat | Không có câu trả lời nào nhắm đúng câu hỏi về việc bị out ra, chỉ có các câu hỏi và thông tin không liên quan  |
| GS-05 | `M00553` | ② | check | need | **TRUOT** | Câu hỏi chưa có câu trả lời nào phù hợp. Tin nhắn 'Mai hỏi luôn nhé [HV]' không phải là câu trả lời cho câu hỏ |
| GS-06 | `M54679` | ② | check | need | **TRUOT** | Không có câu trả lời nào nhắm đúng câu hỏi về thời gian demo và QnA. Các tin nhắn trong 30 phút không liên qua |
| GS-07 | `M30246` | ③ | need | nogrounding | **TRUOT** | Câu hỏi không rõ ràng vì không có thông tin về việc đã gửi mail hay chưa, và không có ai trả lời trước đó. Khô |
| GS-08 | `M27566` | ③ | need | need | dat | Không có câu trả lời nào nhắm đúng câu hỏi của học viên về việc cấp giấy chứng nhận sinh viên. Tin nhắn trong  |
| GS-09 | `M88027` | ③ | check | need | **TRUOT** | Không có câu trả lời nào nhắm đúng câu hỏi về việc gia hạn thời gian nộp Lab2. Các tin nhắn trong kênh không l |
| GS-10 | `M72484` | ④ | need | need | dat | Câu hỏi về hạn nộp Lab02 chưa được giải đáp cụ thể trong các tin nhắn trước đó. BOT đã hướng dẫn kiểm tra các  |
| GS-11 | `M18676` | ④ | check | need | **TRUOT** | Không có câu trả lời nào nhắm đúng câu hỏi 'có điểm danh hả mn :v' trong các tin nhắn trong kênh trong 30 phút |
| GS-12 | `M67980` | ④ | check | need | **TRUOT** | Câu hỏi chưa được giải đáp vì không có câu trả lời nào phù hợp trong các tin nhắn gần đây. Tin nhắn từ người h |
| GS-13 | `M30201` | hiem | need | need | dat | Câu hỏi về điểm chuyên cần chưa có câu trả lời nào phù hợp trong các tin nhắn gần đây. Tin nhắn trả lời gần nh |
| GS-14 | `M36687` | hiem | check | need | **TRUOT** | Không có câu trả lời nào nhắm đúng câu hỏi của học viên. Tin nhắn 'em ké câu hỏi ạ' không phải là câu trả lời  |
| GS-15 | `M19124` | hiem | check | done | **TRUOT** | Câu hỏi đã được trả lời bởi một học viên khác trong cùng kênh, nội dung trả lời liên quan trực tiếp đến câu hỏ |
| GS-16 | `M60122` | thuong | need | need | dat | Không có câu trả lời nào nhắm đúng câu hỏi về daily-standup. Các tin nhắn trong kênh không liên quan đến câu h |
| GS-17 | `M04392` | thuong | need | need | dat | Không có câu trả lời nào nhắm đúng câu hỏi của học viên, vì không có tin nhắn nào trong 'tin_cung_kenh_trong_3 |
| GS-18 | `M03948` | thuong | need | need | dat | Không có câu trả lời nào nhắm đúng câu hỏi về việc không thấy lịch sử bên activity ở kênh Discord. Các tin nhắ |
| GS-19 | `M17206` | thuong | need | nogrounding | **TRUOT** | Câu hỏi không có thông tin rõ ràng về việc đã có ai đó trả lời hay không, và không có nội dung nào trong ngữ c |
| GS-20 | `M18056` | thuong | need | done | **TRUOT** | Câu hỏi 'xem xp ở đâu' đã được trả lời trong tin nhắn của BOT với nội dung hướng dẫn cách theo dõi hoặc tìm ki |
| GS-21 | `M83358` | thuong | done | done | dat | Câu hỏi đã được trả lời đầy đủ bởi D3694 với thông tin rõ ràng về số lượng thành viên trong team. Không có câu |
| GS-22 | `M15562` | thuong | done | check | **TRUOT** | Câu hỏi của học viên về việc hợp tác giữa hai team có thể đã được trả lời nhưng chưa rõ ràng. Câu trả lời từ D |
| GS-23 | `M20982` | thuong | done | need | **TRUOT** | Không có câu trả lời nào nhắm đúng câu hỏi về việc điền hồ sơ năng lực và khả năng bị xem xét kết thúc đào tạo |
| GS-24 | `M49586` | thuong | done | need | **TRUOT** | Câu hỏi không có nội dung cụ thể để trả lời, chỉ là một câu hỏi về việc không có câu hỏi nào để hỏi. Không có  |
| GS-25 | `M83711` | thuong | done | check | **TRUOT** | Câu hỏi chưa được giải đáp rõ ràng. Có hai tin nhắn trả lời, nhưng không có câu trả lời trực tiếp nào xác nhận |

## 5. Phan tich case truot

**GS-02 · `M97637`** — ky vong `nogrounding`, AI tra ve `done`  ·  nguyen nhan nhom **C**  
Nhom gan nhan vi: *Câu hỏi nhắc tới "file hay link" từ một cuộc trò chuyện không có trong kênh đã quét.*  
AI lap luan: *Câu hỏi đã được trả lời đầy đủ bởi BOT trong tin nhắn M08439, cung cấp thông tin chi tiết về quy trình và các link cần thiết. Không có thông tin nào mâu thuẫn và câu hỏi đã được giải đáp rõ ràng.*  
**Chan doan:** BOT tra loi sau 1 phut nen model ket luan done, bo qua viec cau hoi nhac toi 'file hay link' tu mot cuoc tro chuyen khong co trong ngu canh.  
**Huong xu ly:** Buoc 1 phai chay truoc va doc lap voi viec co hay khong co tin tra loi gan.  

**GS-05 · `M00553`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Chỉ được hẹn "mai hỏi luôn", chưa có câu trả lời thật.*  
AI lap luan: *Câu hỏi chưa có câu trả lời nào phù hợp. Tin nhắn 'Mai hỏi luôn nhé [HV]' không phải là câu trả lời cho câu hỏi này mà chỉ là một lời hẹn. Do đó, cần thêm thông tin hoặc câu trả lời từ người khác.*  
_Chua chan doan — doc log `eval/logs/run-02/M00553.json` roi bo sung vao eval/phan_tich.json_  

**GS-06 · `M54679`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Có phản hồi nhưng né câu hỏi; chưa đủ 4 giờ quan sát trước khi dữ liệu kết thúc.*  
AI lap luan: *Không có câu trả lời nào nhắm đúng câu hỏi về thời gian demo và QnA. Các tin nhắn trong 30 phút không liên quan đến câu hỏi này.*  
_Chua chan doan — doc log `eval/logs/run-02/M54679.json` roi bo sung vao eval/phan_tich.json_  

**GS-07 · `M30246`** — ky vong `need`, AI tra ve `nogrounding`  
Nhom gan nhan vi: *Hỏi lại lần 2 sau 3,5 giờ, vẫn không ai trả lời.*  
AI lap luan: *Câu hỏi không rõ ràng vì không có thông tin về việc đã gửi mail hay chưa, và không có ai trả lời trước đó. Không có nội dung nào trong ngữ cảnh để xác định câu hỏi đã được giải đáp hay chưa.*  
_Chua chan doan — doc log `eval/logs/run-02/M30246.json` roi bo sung vao eval/phan_tich.json_  

**GS-09 · `M88027`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Đã được chỉ chỗ gửi ticket sau 13 phút, nhưng chưa rõ yêu cầu gia hạn đã được xử lý chưa.*  
AI lap luan: *Không có câu trả lời nào nhắm đúng câu hỏi về việc gia hạn thời gian nộp Lab2. Các tin nhắn trong kênh không liên quan đến câu hỏi này.*  
_Chua chan doan — doc log `eval/logs/run-02/M88027.json` roi bo sung vao eval/phan_tich.json_  

**GS-11 · `M18676`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Hai bạn học trả lời mâu thuẫn nhau về điểm danh workshop trong cùng buổi sáng.*  
AI lap luan: *Không có câu trả lời nào nhắm đúng câu hỏi 'có điểm danh hả mn :v' trong các tin nhắn trong kênh trong 30 phút qua. Tin nhắn 'không lmao' không liên quan đến câu hỏi này.*  
_Chua chan doan — doc log `eval/logs/run-02/M18676.json` roi bo sung vao eval/phan_tich.json_  

**GS-12 · `M67980`** — ky vong `check`, AI tra ve `need`  
Nhom gan nhan vi: *Học viên phải hỏi lại sau 9 giờ; câu trả lời đến từ bạn học, chưa phải nguồn chính thức.*  
AI lap luan: *Câu hỏi chưa được giải đáp vì không có câu trả lời nào phù hợp trong các tin nhắn gần đây. Tin nhắn từ người hỏi không có phản hồi nào rõ ràng về cách xử lý thẻ ra vào. Cần thêm thông tin từ người khác.*  
_Chua chan doan — doc log `eval/logs/run-02/M67980.json` roi bo sung vao eval/phan_tich.json_  

**GS-14 · `M36687`** — ky vong `check`, AI tra ve `need`  ·  nguyen nhan nhom **D**  
Nhom gan nhan vi: *Có trả lời, nhưng sau gần 12 giờ và qua câu hỏi "ké" của người khác.*  
AI lap luan: *Không có câu trả lời nào nhắm đúng câu hỏi của học viên. Tin nhắn 'em ké câu hỏi ạ' không phải là câu trả lời cho câu hỏi về group tập gym hay bơi. Cần thêm thông tin từ người khác.*  
**Chan doan:** Cau tra loi den sau 705 phut qua cau hoi 'ke' cua nguoi khac — nam ngoai moi cua so thoi gian hop ly.  
**Huong xu ly:** Khong sua bang prompt. Can tim kiem theo ngu nghia thay vi theo thoi gian; de lai sau CP3.  

**GS-15 · `M19124`** — ky vong `check`, AI tra ve `done`  ·  nguyen nhan nhom **E**  
Nhom gan nhan vi: *Có trả lời, nhưng sau 8 giờ.*  
AI lap luan: *Câu hỏi đã được trả lời bởi một học viên khác trong cùng kênh, nội dung trả lời liên quan trực tiếp đến câu hỏi về deadline ghép đội tự do. Căn cứ vào bước 2, có câu trả lời phù hợp.*  
**Chan doan:** Luot 5 da them sau_bao_phut = 487 vao reply truc tiep, nhung model van viet 'trong vong 2 gio'. Day la loi tuan thu, khong phai thieu du lieu.  
**Huong xu ly:** Tinh san co 'tra_loi_muon: true' trong code thay vi de model tu so sanh so.  

**GS-19 · `M17206`** — ky vong `need`, AI tra ve `nogrounding`  
Nhom gan nhan vi: *Không TA/BTC nào phản hồi, có người +1.*  
AI lap luan: *Câu hỏi không có thông tin rõ ràng về việc đã có ai đó trả lời hay không, và không có nội dung nào trong ngữ cảnh đề cập đến câu hỏi này. Không thể kết luận được câu hỏi đã được giải đáp hay chưa.*  
_Chua chan doan — doc log `eval/logs/run-02/M17206.json` roi bo sung vao eval/phan_tich.json_  

**GS-20 · `M18056`** — ky vong `need`, AI tra ve `done`  ·  nguyen nhan nhom **F**  
Nhom gan nhan vi: *2 người hỏi cách xem XP trong cùng buổi chiều, không ai trả lời.*  
AI lap luan: *Câu hỏi 'xem xp ở đâu' đã được trả lời trong tin nhắn của BOT với nội dung hướng dẫn cách theo dõi hoặc tìm kiếm điểm XP. Tin nhắn này nằm trong 'tin_cung_kenh_trong_30_phut'.*  
**Chan doan:** Cau hoi giong het cua nguoi khac da duoc BOT tra loi 19 phut truoc trong cung kenh. Ca nhom va AI deu doc dung du lieu — khac nhau o dinh nghia san pham.  
**Huong xu ly:** Nhom phai chot truoc CP4: xep need, check, hay them trang thai 'da co dap an, chi can tro'.  

**GS-22 · `M15562`** — ky vong `done`, AI tra ve `check`  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M45489)*  
AI lap luan: *Câu hỏi của học viên về việc hợp tác giữa hai team có thể đã được trả lời nhưng chưa rõ ràng. Câu trả lời từ D3694 không trực tiếp giải quyết câu hỏi về việc bắt tay giữa hai team mà chỉ đưa ra ý kiến về việc tìm đồng đội. Cần kiểm tra thêm để xác định có câu trả lời nào khác rõ ràng hơn không.*  
_Chua chan doan — doc log `eval/logs/run-02/M15562.json` roi bo sung vao eval/phan_tich.json_  

**GS-23 · `M20982`** — ky vong `done`, AI tra ve `need`  ·  nguyen nhan nhom **A**  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M92726)*  
AI lap luan: *Không có câu trả lời nào nhắm đúng câu hỏi về việc điền hồ sơ năng lực và khả năng bị xem xét kết thúc đào tạo sớm. Các tin nhắn trong 30 phút không liên quan đến câu hỏi này.*  
**Chan doan:** Co tra loi nhung model danh gia la chua du ro nen ha xuong check. Bang chung mong, ranh gioi done/check con mo.  
**Huong xu ly:** Bo sung tieu chi 'du de nguoi hoi di tiep' vao dinh nghia done.  

**GS-24 · `M49586`** — ky vong `done`, AI tra ve `need`  ·  nguyen nhan nhom **G**  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M17083)*  
AI lap luan: *Câu hỏi không có nội dung cụ thể để trả lời, chỉ là một câu hỏi về việc không có câu hỏi nào để hỏi. Không có câu trả lời nào nhắm đúng vào câu hỏi này trong kênh.*  
**Chan doan:** Tin la 'Kieu em ko co cau hoi nao hoi, co on ko a :))' — khong phai cau hoi can nguoi tra loi. Bon nhan hien tai khong co cho de xep.  
**Huong xu ly:** Them nhan thu nam 'khong phai cau hoi', hoac quy uoc xep vao done kem ly do.  

**GS-25 · `M83711`** — ky vong `done`, AI tra ve `check`  
Nhom gan nhan vi: *(nhan chi ghi tin lam can cu: M81490)*  
AI lap luan: *Câu hỏi chưa được giải đáp rõ ràng. Có hai tin nhắn trả lời, nhưng không có câu trả lời trực tiếp nào xác nhận việc bài mới đã được up hay chưa. Tin nhắn từ D7688 chỉ hướng dẫn hỏi labcoach, không trả lời trực tiếp câu hỏi. Tin nhắn từ D6604 có thể là câu trả lời nhưng không rõ ràng vì không có thông tin cụ thể về bài mới. Cần kiểm tra thêm để xác nhận.*  
_Chua chan doan — doc log `eval/logs/run-02/M83711.json` roi bo sung vao eval/phan_tich.json_  

### Gom theo nhom nguyen nhan

| Nhom | So case | Mo ta |
|---|---|---|
| **A** | 1 | Ranh gioi need/check: nhom coi reply lac de hoac '+1' la KHONG ai dung toi (need); model coi co reply la da dung toi (check). |
| **C** | 1 | nogrounding bi lan at: khi co bat ky tin tra loi nao o gan, model bo qua buoc 1 va khong con hoi 'can cu co nam trong tam quan sat khong'. |
| **D** | 1 | Cua so thoi gian: cau tra loi den ngoai +/-30 phut thi khong bao gio vao ngu canh. Day la gioi han thiet ke, khong sua duoc bang prompt. |
| **E** | 1 | Model doc sai du lieu da duoc cung cap (vi du bo qua truong sau_bao_phut). |
| **F** | 1 | Ranh gioi san pham chua dinh nghia: dap an da co san trong kenh cho cau hoi giong het cua nguoi khac. |
| **G** | 1 | Thieu nhan thu nam cho 'khong phai cau hoi can nguoi tra loi'. |


## 6. Doi chieu quality bar

Quality bar (chot tai CP4, xem `spec.md` §7): bo sot <=1/20 cau that su bo ngo (recall >=95%),
bao thua <=30%, va 0 muc lo ten nguoi.

- Recall luot nay: **88.2%** — CHUA DAT
- Bao thua: **16.0%** — DAT
- Lo ten nguoi: **0** — ban tin chi xuat `msg_id` va link, khong xuat tac gia
