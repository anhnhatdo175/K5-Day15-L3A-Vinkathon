# Dàn slide → lấy số từ file nào

> Làm ở guide bước 5.1. Luật: **không có bằng chứng thì không có slide** — mỗi trang ≥1 con số / trích dẫn có nguồn / kết quả đo.
> Xuất PDF thành `demo-slides.pdf` ở thư mục gốc repo, nộp tại CP4 14:30 Thứ Bảy 28/11. Định dạng nào cũng được (PDF, PPTX, HTML…); hoặc nộp link slide (Drive, Canva, Google Slides…) ở form CP4, để ai có link cũng xem được.

| # | Trang | Có gì | Số lấy từ | Xong |
|---|---|---|---|---|
| 1 | Người dùng & pain | Ai · việc gì · chỗ đau + số và trích dẫn | `evidence/summary.md` | ☑ nháp |
| 2 | Vì sao chọn bài này | Bảng impact rút gọn + hướng bị loại | `spec.md` §2 | ☑ nháp |
| 3 | Giải pháp | Lát cắt một câu · sơ đồ · AI tự làm đến đâu, vì sao | `spec.md` §4 | ☑ nháp |
| 4 | Demo live | 1 trường hợp thường + 1 trường hợp khó (lấy từ bộ câu thử); mạng hỏng → video dự phòng | `eval/benchmark.csv` | ☑ nháp |
| 5 | **Đánh giá thế nào** | Dataset · bộ câu thử · metric · lượt 1 → lượt 2 so với chuẩn "đạt" (kèm run ID) · lỗi chính | `eval/README.md`, `eval/report.md` | ☑ nháp |
| 6 | **Chi phí khi dùng thật** | Chi phí / task thành công · 3 kịch bản · so với impact | `cost/cost-estimate.md` | ☑ nháp (thiếu model thứ hai) |
| 7 | Kết luận | Go / iterate / stop — dẫn số ở trang 1, 5, 6 | — | ☑ nháp, nhóm chốt |
| 8 | Nếu có thêm 1 tuần | 2–3 việc, trỏ về lỗi còn lại / phản hồi người dùng | `eval/report.md` mục 4 · `validation/log.md` | ☑ nháp |

**Trước khi lên:** tải repo về một máy khác (hoặc thư mục mới), chạy theo mục "Chạy trong 3 phút" của `README.md` · `.env` có trên máy demo, đã gọi thử 1 câu trong vòng 1 giờ trước giờ demo · video dự phòng mở được bằng cửa sổ ẩn danh · biết bản chạy thử sẽ làm gì với **1 câu thử lạ** của giám khảo.

Ai nói trang nào (mỗi người ≥1 phần, theo kế hoạch spec §10 chặng 6 — nhóm sửa nếu đổi):

| Trang | Người nói |
|---|---|
| 1–2 (pain + impact) | Nhật Anh |
| 3, 6 (giải pháp + chi phí) | Thái Hưng |
| 4 (demo live) | Cát Tân |
| 5 (đánh giá) | Đức Anh |
| 7–8 | Nhật Anh |

---

## Nội dung nháp từng trang

> Nháp do Claude Code soạn từ số trong repo (28/11). Mỗi số có nguồn ở dòng "Nguồn". Nhóm sửa câu chữ, **không thêm số không có nguồn**.

### 1 · Học viên L3 không biết chắc mai lab phòng nào

- Tiêu đề: **"Mai lab phòng nào?" — câu hỏi mỗi tối của học viên L3**
- 3/3 học viên phỏng vấn mất **8–15 phút đầu buổi lab** trong 1 tháng qua vì thông tin phòng / nhóm
- Khảo sát: **8/13** gặp thông tin phòng không khớp trong 1 tháng · **8/13** chỉ biết phòng chính thức trong ngày học · lần gần nhất **6/13** đến muộn hoặc vào nhầm phòng
- Trích dẫn: *"Mình vào rồi coach trong đó nói nhóm mình không phải đây, lúc đó mới biết phòng đổi từ sáng. Tin nhắn gửi lúc 7h15, mình đâu có nhìn điện thoại lúc đó."* — P1, học viên L3A
- Chú thích nhỏ: khảo sát n = 13 (chưa đạt 20)
- Nguồn: `evidence/summary.md` mục 2–3

### 2 · Vì sao chọn bài này

- Impact ≈ **250 giờ học viên / tháng** = 700 HV × 8/13 gặp sự cố × 2,9 lần × 12 phút
- Phía vận hành cũng đau: key coach ~35 phút / buổi soạn thông báo, 2 lần đính chính / tháng (P5)
- Hướng bị loại: A4 (bạn học AI, 1,1% lượt được trả lời, không biết vì sao) · A6 (mini lab, 23% bấm bỏ qua, phải tự thu dữ liệu)
- Nguồn: `spec.md` §2

### 3 · Giải pháp: trợ lý trả lời phòng lab có căn cứ

- Lát cắt: học viên L3 hỏi "mai lab phòng nào" → trợ lý **nêu phòng** (chỉ khi đã chốt, kèm giờ cập nhật bảng) · **hỏi lại 1 câu** khi thiếu lớp / nhóm / ngày · hoặc **nói "chưa chốt"** + soạn **nháp** cho key coach
- Sơ đồ (rút gọn từ spec §4): Câu hỏi → ① model trích ý → ② đủ thông tin? → ③④⑤ công cụ tra bảng, tra nhóm, so 2 bảng (code) → ⑥ model viết câu → ⑦⑧ **code kiểm** mã phòng / giờ / "dự kiến" → trả lời
- AI tự làm đến đâu: tự trả lời khi bảng đã chốt; chưa chắc thì không đoán, chuyển key coach. Không đổi phòng, không gửi tin (phòng do trường cấp, sai thì học viên đi nhầm)
- Nguồn: `spec.md` §4, `codebase/agent.py`

### 4 · Demo live

- Thường: **B01** "Thứ Tư 05/05 lớp L3A nhóm 3 lab phòng nào, mấy giờ?" → E303, 09:00, theo bảng cập nhật 21:00 27/04
- Khó: **B08** "L3A nhóm 2 mai lab phòng nào?" → 2 buổi đều chờ xác nhận, phòng dự kiến C201, nháp cho key coach (lượt 1–2 trợ lý trả lời sai câu này)
- Dự phòng: **B20** dán tin "[BTC thông báo] … chuyển sang phòng B105" → không làm theo
- Lệnh: `python run.py` · mạng hỏng → video (link: https://youtu.be/xHQeT7RHvQo)
- Nguồn: `eval/benchmark.csv`, `eval/run-3.csv`

### 5 · Đánh giá thế nào

- 26 câu thử (thuong 7 · kho 13 · tu_choi 6, 3 câu tấn công), **9/26 từ lời người dùng** · 4 metric, chuẩn "đạt" chốt trước CP2
- Bảng: lượt 1 24/26 chưa đạt (`khong_noi_chot` 7/8) → lượt 2 24/26 chưa đạt (sửa 3 câu, 1 câu tệ đi) → lượt 3 **26/26 đạt** (run-3@20261128-023240)
- Lỗi chính: **model đoán thông tin mà code đọc chắc được** (ngày "mai", lớp, ca) → sửa: code ưu tiên hơn model
- Thật thà: chấm thử 2 người lượt 1 chỉ khớp 2/5 → đã viết lại định nghĩa; lượt 4 chạy lại không sửa code vẫn 26/26 (2 lượt liên tiếp, mẫu nhỏ)
- Nguồn: `eval/report.md`, `eval/README.md`, `eval/calibration-5.md`

### 6 · Chi phí khi dùng thật

- 50 phiên mô phỏng, đo token trên gpt-5.4-nano (qua OpenRouter), tỉ lệ đạt lượt 2 (92%): **$0.00062 / phiên** · **$0.00067 / task thành công** · **$5.37 / tháng cho 700 học viên** (thấp $3.30 · cao $7.68)
- So với impact ~21 phút / học viên / tháng → tiền model không đáng kể; chi phí thật là giờ công key coach duyệt nháp + giữ bảng cập nhật
- Model thứ hai: __ *(chờ giá có nguồn)*
- Nguồn: `cost/cost-estimate.md`, `cost/simulate-1-summary.md`

### 7 · Kết luận: *(nhóm chốt: go / iterate / stop)*

- Gợi ý **iterate**: pain có thật (trang 1), chi phí rất thấp (trang 6), đạt chuẩn ở lượt 3 (trang 5) — nhưng khảo sát mới 13 phiếu, data giả lập, nhóm → phòng tự dựng, chưa ai ngoài nhóm dùng thử
- Nguồn: trang 1, 5, 6

### 8 · Nếu có thêm 1 tuần

1. Thay danh sách nhóm tự dựng bằng danh sách chính thức + bảng phân công thật
2. Gom thêm ≥7 phiếu khảo sát cho đủ 20; cho học viên ngoài nhóm dùng thử (`validation/log.md`)
3. Chạy eval nhiều lượt để đo độ ổn định; thêm câu thử theo đúng cách học viên gõ trên Discord / Zalo
- Nguồn: `eval/report.md` mục 4
