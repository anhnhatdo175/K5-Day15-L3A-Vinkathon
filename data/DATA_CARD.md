# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

**Bản đầu CP2 (27/11 19:10) · bản CP3 (28/11 ~02:00):** data lịch đã tách vào `data/` bằng `python data/build_data.py`.

## Dataset 1 · Bảng lịch lab chạy thử (tách từ bộ giả lập `training-ops`)

| | |
|---|---|
| Dùng để làm gì | nguồn cho công cụ `get_schedule`, `check_conflicts` (spec §4) · giá trị phòng, giờ, giờ cập nhật bảng trong `eval/benchmark.csv` |
| Từ đâu | data BTC cấp: `data/training-ops/` của repo đề (README + `teaching-schedule.xlsx` + `lab-coach-schedule.xlsx`), **giả lập**. Nguyên file để ở `data-btc/` (đã có trong `.gitignore`), không commit |
| Xử lý những bước gì | script `data/build_data.py` (chỉ dùng thư viện chuẩn, chạy lại ra cùng kết quả): (1) sheet `Khoá 9 (GĐ1)` cột F (LAB của L3) → `lich_chinh_thuc.csv`: mỗi buổi LAB của L3A / L3B một dòng: ngày, ca, lớp, buổi, giờ bắt đầu–kết thúc (giờ riêng nếu ô có), trạng thái (`chot` / `cho_xac_nhan`), phòng đã chốt hoặc phòng dự kiến, chủ đề, giờ sửa ô lần cuối, giờ xuất bảng (21:00 27/04/2027, ô D1) · (2) `lab-coach-schedule.xlsx` → `lich_lab_coach.csv`: phòng của cùng các buổi trong sheet `Lịch lab 2604-0805` (cột K–P; `dk:` = dự kiến) và bản chép lịch 12/04 · (3) sheet `Lịch sử chỉnh sửa` → `lich_su_sua.csv`: các lần sửa ô LAB của L3 · bỏ tên giảng viên / lab coach, email, link (trợ lý không cần) |
| Số dòng / số đoạn | `lich_chinh_thuc.csv` 28 buổi LAB (25 `chot`, 3 `cho_xac_nhan`) · `lich_lab_coach.csv` 41 dòng (13 từ lịch lab đợt 2, 28 từ bản chép 12/04) · `lich_su_sua.csv` 18 lần sửa |
| Phiên bản / ngày lấy | bản xuất bảng phân công 21:00 27/04/2027 (theo data giả lập) · lấy từ repo đề 28/11/2026 |
| Nhãn | `synthetic` (BTC giả lập) |
| Mốc "hôm nay" khi chạy thử | **Chủ nhật 02/05/2027 tối** (đặt trong code). Bảng vẫn là bản xuất 27/04, nên câu trả lời nêu "theo bảng cập nhật lúc 21:00 27/04". Chọn mốc này vì ngày mai (03/05) L3A có buổi chờ xác nhận, và sau đó có buổi đã chốt của cả hai lớp (05/05, 06/05) |
| Giới hạn | giả lập: tần suất phòng đổi / chờ xác nhận trong bảng **không** phản ánh thực tế, không dùng làm bằng chứng pain · mã phòng giả lập (C203, H201…) không phải mã phòng nghe trong phỏng vấn (A.301, B.205…) · **data không có buổi LAB online** (chỉ có LEC L3AB online), nên câu thử B10 hỏi về buổi không có lab · L3B không có buổi lab sáng nào |

## Dataset 1b · Danh sách nhóm và quy tắc nhóm → phòng (`data/nhom.csv`), TỰ DỰNG

| | |
|---|---|
| Dùng để làm gì | nguồn cho `find_group` (tra nhóm theo số nhóm hoặc tên) và cho việc chọn phòng của một nhóm trong danh sách phòng của buổi |
| Từ đâu | **nhóm tự sinh**, vì data BTC **không có bảng nhóm → phòng**: mỗi buổi LAB ghi một danh sách 3–6 phòng cho cả lớp (~350 HV, "1 GV/nhóm, phủ mọi phòng lab") |
| Xử lý những bước gì | `build_data.py`: 12 nhóm / lớp *(tự ước tính)*, mỗi nhóm 4 tên mẫu ghép từ danh sách họ, đệm, tên phổ biến, không trùng nhau, **không phải người thật**. Quy tắc phòng: nhóm *g* ngồi phòng thứ ((*g*−1) mod *k*) + 1 trong danh sách *k* phòng của buổi đó (theo thứ tự ghi trong ô lịch) |
| Số dòng | 96 (2 lớp × 12 nhóm × 4 tên) |
| Nhãn | `synthetic` (nhóm tự sinh, không seed ngẫu nhiên: quy tắc cố định) |
| Giới hạn | quy tắc nhóm → phòng là giả định của nhóm, không lấy từ khoá thật; ngoài đời phải thay bằng danh sách nhóm chính thức |

## Dataset 2 · Ghi chép phỏng vấn P1–P5 (nguồn câu thử `nguoi_dung`)

| | |
|---|---|
| Dùng để làm gì | bộ câu thử: B17 (P1), B18 (P3), B19 (P2, P5) lấy tình huống từ lời người dùng; B20 gợi từ P4, P5 · đặt kịch bản spec §5 · lý do của metric (`why` trong `eval/metric_spec.yaml`) |
| Từ đâu | nhóm tự phỏng vấn trực tiếp 27/11 16:40–18:10 theo `evidence/interviews/GUIDE-A5.md`: 3 học viên L3 (P1, P2 L3A · P3 L3B), 1 lab coach (P4), 1 key coach (P5), đều ngoài nhóm |
| Xử lý những bước gì | ghi theo `evidence/interviews/TEMPLATE.md` · ẩn danh: chỉ ghi vai, người hỏi ghi TV1–TV4, không tên, không liên lạc · câu thử viết lại tình huống, thay mã phòng thật bằng chỗ `[điền từ data]` |
| Số dòng / số đoạn | 5 file (`evidence/interviews/P1.md`–`P5.md`) |
| Phiên bản / ngày lấy | 27/11/2026 · commit `333fb18` |
| Nhãn | thật |
| Giới hạn | n nhỏ (3 học viên), cùng một khoá, gặp tại lớp chiều 27/11 → lệch về người đi lab trực tiếp hôm đó; P4 và P5 kể cùng một sự cố 17/11 (không cộng 2 lần) |

## Dataset 3 · Bảng mẫu chấm thử (`eval/calibration-5.md`)

| | |
|---|---|
| Dùng để làm gì | chỉ để hai người chấm thử 5 output, kiểm định nghĩa metric trước CP2 |
| Từ đâu | nhóm tự dựng (Claude Code soạn, 3 dòng, mã phòng dạng `P-xxx` không có thật) |
| Nhãn | `synthetic` |
| Giới hạn | không dùng trong bản chạy thử, không dùng trong `run.py eval`, không phải bằng chứng |

**Data `synthetic` (nhóm tự sinh):** Dataset 3 soạn tay, không seed; người kiểm: __, kiểm tay __/3 dòng. Data tự dựng **không phải bằng chứng pain**.

*Không dùng cho bản chạy thử:* `data/preclass/` (BTC, để ở `data-btc/preclass/`) chỉ dùng đào số cho bảng so sánh hướng ở spec §2 (`evidence/data-mining.md`).
