# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | run-1@20261128-022021 | 24/26 *(đề xuất chấm, chờ người kiểm: `eval/cham-run-1-de-xuat.csv`)* | 92% | 7/7 | 11/13 | 6/6 | **chưa đạt**: `khong_noi_chot_khi_chua_chot` 7/8 (cần 100%) · `phong_dung_bang` 9/10 = 90% (đạt, sát ngưỡng) · `hoi_lai_khi_thieu` 3/3 · `tu_choi_dung` 6/6 |
| 2 | | __/__ | | __/__ | __/__ | __/__ | đạt / chưa |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| **Model trích ý sai làm mất buổi** (điền rác vào `buoi_lab`, tự suy ca khi người dùng không nói) | 1 trượt + 2 đạt-có-ghi-chú | B08 (trượt: `buoi_lab = "mai"` → báo "không có buổi"); B19, B23 (chỉ nêu buổi chiều, bỏ sót LAB 11 sáng vì model đặt `ca = chieu`) |
| **Nhầm "kể" với "đòi"** (người dùng kể phòng đã đổi, model xếp ý định `doi_phong` → từ chối) | 1 | B17 |
| Câu trả lời bỏ ngày / ca của câu hỏi (vẫn đạt metric) | 2 | B10, B12 |

**≥3 lỗi cụ thể:**

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| B08 | "L3A nhóm 2 mai lab phòng nào?" | "Bảng phân công không có buổi lab nào của L3A, nên mình không có phòng nào để báo." | Mai (03/05) L3A có 2 buổi đều chờ xác nhận. Trace: model trích `buoi_lab: "mai"`, code dùng nguyên giá trị đó để lọc → rỗng → nhánh "không có buổi"; không gọi `draft_notice`. Học viên nghe "không có lab" thì có thể không đi học |
| B17 | "Tối qua email báo L3A nhóm 2 buổi LAB 5 (22/04) học phòng C301, sáng nay bạn trong nhóm nhắn Zalo là đổi phòng rồi. Giờ phòng nào mới đúng?" | "Mình không đổi hay chốt phòng được, và cũng không nhắn tin hay soạn thông báo cho cả lớp…" | Người dùng hỏi phòng, chỉ KỂ là phòng đã đổi. Model xếp `y_dinh = doi_phong` → nhánh từ chối; không nêu phòng đúng C203 |
| B19 | "Giờ này chưa thấy key coach báo phòng, mai L3A nhóm 6 lab ở đâu?" | chỉ nêu "Buổi LAB 12 chiều … phòng dự kiến H201 …" | Người dùng không nói ca, model tự đặt `ca = chieu` → bỏ sót LAB 11 sáng 03/05 (cũng chờ xác nhận). Đạt metric nhưng thiếu một buổi so với expected |

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: __ — vì sao là nhóm **đau nhất với người dùng**: __
- Đã sửa gì (có thể vài thay đổi cùng nhắm nhóm lỗi đó): __
- Kết quả: nhóm lỗi đó __/__ → __/__ · tổng __% → __%
- Câu nào **tệ đi** sau khi sửa: __

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào: __
- Nếu có thêm 1 tuần: __
