# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): ≥3 kiểu — tỉ lệ, số phiên / người / tháng, số lượt hỏi / phiên. Nguồn: khảo sát A2 (n = 13): dùng ít 0,31 · 1 phiên / tháng *(tự ước tính)* · 1 lượt; dùng vừa 0,38 · 10 phiên · 2 lượt; dùng nhiều 0,31 · 20 phiên · 2 lượt (số lượt / phiên: *tự ước tính*)
- **Số người dùng thật** 3 kịch bản: thấp 430 · cơ sở 700 · cao 1.000. Nguồn: cơ sở = lớp L3 hơn 700 học viên (file track A, mục A5); thấp = 700 × 8/13 (khảo sát A7); cao *(tự ước tính)*
- **Giá** ≥2 mức model (từ `further-reading/model-prices.md` của repo đề, có link + ngày xem): gpt-5.4-nano: vào $0.20 · ra $1.25 / 1M token, https://developers.openai.com/api/docs/pricing?latest-pricing-expanded=true, xem 28/11/2026 (trang ghi model này *Deprecated*) · **gpt-5.4-mini** (mức mạnh hơn, cùng hãng): vào $0.75 · ra $4.50 / 1M token (cached input $0.075, không dùng), cùng trang giá, bảng "Standard", xem 28/11/2026 ~04:10
- **Tỉ lệ đạt** dùng để tính: **24/26 (92%), lượt 2 `run-2@20261128-022855`** (`python run.py simulate --rate-from eval/run-2.csv`, đúng lệnh CP4). Lượt 3 (26/26) không dùng để tính vì là lượt thêm sau lượt 2; nếu dùng thì chi phí / task thành công là $0.00062 (`simulate-1`, xem cuối mục 2)
- Đo token trên **openai/gpt-5.4-nano qua OpenRouter**, tính giá model gpt-5.4-nano. Cùng một model với lượt 2 (lượt 2 gọi thẳng OpenAI API), chỉ khác đường gọi, nên simulate báo "khác model" chỉ vì tên ghi khác (`spec.md` §10, 28/11 ~03:40). **gpt-5.4-mini: không chạy lại**, tính giá mini trên chính token đo ở `simulate-2` (đo trên gpt-5.4-nano, tính giá gpt-5.4-mini), cùng công thức của `cost/simulate.py`; kiểm công thức bằng cách tính lại dòng nano ra đúng số trong `simulate-2-summary.md`. Hai model cùng hãng, cùng bộ tách token nên lệch token nhỏ; chưa đo tỉ lệ đạt riêng của mini nên dùng tạm tỉ lệ đạt lượt 2 của nano

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-2.csv` · run ID simulate-2@20261128-035352 · 50 phiên (0 lỗi) · seed 42 · tỉ lệ đạt từ lượt 2 (`--rate-from eval/run-2.csv`) · bảng chép từ `cost/simulate-2-summary.md`

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 18 | 1 | 1072 | 136 | 1.8 | 3.1 |
| dung_vua | 16 | 2 | 2158 | 252 | 3.8 | 6.3 |
| dung_nhieu | 16 | 2 | 2208 | 256 | 3.8 | 6.1 |

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp | / tháng — cơ sở | / tháng — cao | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| gpt-5.4-nano (vào 0.2 · ra 1.25 $/1M) | $0.00062 | **$0.00067** (lượt 2, 92%) | $3.30 | $5.37 | $7.68 | $0.0077 |
| gpt-5.4-mini (vào 0.75 · ra 4.50 $/1M) *(token đo trên nano, tính lại theo giá mini)* | $0.00229 | $0.00248 (tỉ lệ đạt lượt 2 của nano) | $12.17 | $19.81 | $28.31 | $0.0283 |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**.

Lần mô phỏng trước (`cost/simulate-1.csv`, simulate-1@20261128-024111, token đo khi gọi thẳng OpenAI, tỉ lệ đạt lượt 3 = 100%): $0.00062 / phiên · $0.00062 / task thành công · $3.29 / $5.35 / $7.64 / tháng · $0.0076 / người / tháng. Token / phiên hai lần lệch dưới 1%, nên chênh lệch chủ yếu do tỉ lệ đạt.

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): ≈ 250 giờ / 700 học viên ≈ **21 phút / học viên / tháng** (cơ sở); với người có gặp sự cố: 2,9 lần × 12 phút ≈ 35 phút / tháng
- Chi phí / người / tháng (cơ sở, model gpt-5.4-nano, tỉ lệ đạt lượt 2): **$0.0077** (≈ $5.37 / tháng cho 700 người) · nếu đổi sang gpt-5.4-mini: $0.0283 (≈ $19.81 / tháng), đắt gấp ~3,7 lần nhưng vẫn rất nhỏ so với impact
- **Kết luận một dòng — đáng làm không:** chi phí model gần như bằng 0 so với ~21 phút học viên / người / tháng; cái đắt thật là giờ công key coach duyệt bản nháp `draft_notice` và việc giữ bảng phân công cập nhật (chưa tính), và độ tin của impact (khảo sát mới 13 phiếu).

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
