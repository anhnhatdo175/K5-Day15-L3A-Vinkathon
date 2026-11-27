# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): ≥3 kiểu — tỉ lệ, số phiên / người / tháng, số lượt hỏi / phiên. Nguồn: khảo sát A2 (n = 13): dùng ít 0,31 · 1 phiên / tháng *(tự ước tính)* · 1 lượt; dùng vừa 0,38 · 10 phiên · 2 lượt; dùng nhiều 0,31 · 20 phiên · 2 lượt (số lượt / phiên: *tự ước tính*)
- **Số người dùng thật** 3 kịch bản: thấp 430 · cơ sở 700 · cao 1.000. Nguồn: cơ sở = lớp L3 hơn 700 học viên (file track A, mục A5); thấp = 700 × 8/13 (khảo sát A7); cao *(tự ước tính)*
- **Giá** ≥2 mức model (từ `further-reading/model-prices.md` của repo đề, có link + ngày xem): gpt-5.4-nano: vào $0.20 · ra $1.25 / 1M token, https://developers.openai.com/api/docs/pricing?latest-pricing-expanded=true, xem 28/11/2026 (trang ghi model này *Deprecated*) · **model thứ hai: chưa có giá có nguồn** (cần bổ sung trước CP4)
- **Tỉ lệ đạt** dùng để tính: 26/26 (100%) — lượt `run-3@20261128-023240` (khung tự chọn lượt mới nhất đã chấm). Với lượt 2 (24/26 = 92%): chi phí / task thành công = $0.00062 ÷ 0,923 ≈ **$0.00067**
- Đo token trên model gpt-5.4-nano, tính giá model gpt-5.4-nano (chưa có model thứ hai)

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID simulate-1@20261128-024111 · 50 phiên (0 lỗi) · seed 42

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 18 | 1 | 1072 | 139 | 1.8 | 3.1 |
| dung_vua | 16 | 2 | 2149 | 243 | 3.8 | 6.2 |
| dung_nhieu | 16 | 2 | 2198 | 259 | 3.8 | 6.0 |

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp | / tháng — cơ sở | / tháng — cao | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| gpt-5.4-nano (vào 0.2 · ra 1.25 $/1M) | $0.00062 | $0.00062 (lượt 3) · $0.00067 (lượt 2) | $3.29 | $5.35 | $7.64 | $0.0076 |
| *(model thứ hai — chưa có giá)* | | | | | | |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**.

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): ≈ 250 giờ / 700 học viên ≈ **21 phút / học viên / tháng** (cơ sở); với người có gặp sự cố: 2,9 lần × 12 phút ≈ 35 phút / tháng
- Chi phí / người / tháng (cơ sở, model gpt-5.4-nano): **$0.0076** (≈ $5.35 / tháng cho 700 người)
- **Kết luận một dòng — đáng làm không:** chi phí model gần như bằng 0 so với ~21 phút học viên / người / tháng; cái đắt thật là giờ công key coach duyệt bản nháp `draft_notice` và việc giữ bảng phân công cập nhật (chưa tính), và độ tin của impact (khảo sát mới 13 phiếu).

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
