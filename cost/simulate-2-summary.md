# Tóm tắt mô phỏng simulate-2@20261128-035352

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 18 | 1 | 1072 | 136 | 1.8 | 3.1 |
| dung_vua | 16 | 2 | 2158 | 252 | 3.8 | 6.3 |
| dung_nhieu | 16 | 2 | 2208 | 256 | 3.8 | 6.1 |

Tỉ lệ đạt dùng để tính: 24/26 (92%) — lượt run-2@20261128-022855

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from). ⚠️ Lượt này chạy bằng gpt-5.4-nano, mô phỏng đo trên openai/gpt-5.4-nano — khác model.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (430 người) | Chi phí / tháng — cơ sở (700 người) | Chi phí / tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.4-nano (vào 0.2 · ra 1.25 $/1M) | $0.00062 | $0.00067 | $0.00041 | $3.30 | $5.37 | $7.68 | $0.0077 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.6) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: openai/gpt-5.4-nano. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
