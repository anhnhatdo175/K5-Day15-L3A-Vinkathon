# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

**Bản đầu CP2 (27/11 19:10).** Chỗ còn `__` điền khi Thái Hưng đưa data lịch chạy thử vào `data/` (CP3).

## Dataset 1 · Bảng lịch lab chạy thử (tách từ bộ giả lập `training-ops`)

| | |
|---|---|
| Dùng để làm gì | nguồn cho công cụ `get_schedule`, `find_group`, `check_conflicts` (spec §4) · điền phần `[điền từ data]` trong `eval/benchmark.csv` (phòng, giờ, giờ cập nhật bảng của từng câu) |
| Từ đâu | data BTC cấp: `data/training-ops/` của repo đề (README + 2 file xlsx) — **giả lập**; nguyên file để ở `data-btc/`, không commit |
| Xử lý những bước gì | lọc buổi lab của L3A / L3B · tách mỗi ô lịch thành cột: lớp, nhóm, buổi, ngày, phòng, trạng thái (`chot` / `cho_xac_nhan` / `online`), giờ bắt đầu, giờ cập nhật bảng, bảng nguồn (bảng chính thức / bảng lab coach) · giữ các kiểu ô Thái Hưng ghi ở chặng 1: phòng đã chốt, "dự kiến", "chờ xác nhận", online, giờ riêng, nghỉ lễ · ẩn danh: không có tên học viên (script: `__`, Thái Hưng) |
| Số dòng / số đoạn | __ |
| Phiên bản / ngày lấy | __ |
| Nhãn | `synthetic` (BTC giả lập) |
| Giới hạn | giả lập: tần suất phòng đổi / chờ xác nhận trong bảng **không** phản ánh thực tế, không dùng làm bằng chứng pain; mã phòng giả lập không trùng mã phòng thật nghe trong phỏng vấn (A.301, B.205…) |

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
