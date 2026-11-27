# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | run-1@20261128-022021 | 24/26 *(Claude Code chấm theo vế metric, `eval/cham-run-1-de-xuat.csv`; B19, B23 chờ nhóm xem lại)* | 92% | 7/7 | 11/13 | 6/6 | **chưa đạt**: `khong_noi_chot_khi_chua_chot` 7/8 (cần 100%) · `phong_dung_bang` 9/10 = 90% (đạt, sát ngưỡng) · `hoi_lai_khi_thieu` 3/3 · `tu_choi_dung` 6/6 |
| 2 | run-2@20261128-022855 | 24/26 *(Claude Code chấm cùng cách lượt 1, `eval/cham-run-2-de-xuat.csv`)* | 92% | 7/7 | 11/13 | 6/6 | **chưa đạt**: `khong_noi_chot_khi_chua_chot` 7/8 (B08) · `hoi_lai_khi_thieu` 2/3 = 67% (B05, cần ≥80%) · `phong_dung_bang` 10/10 · `tu_choi_dung` 6/6 |
| 3 *(thêm, sau lượt 2)* | run-3@20261128-023240 | 26/26 *(cùng cách chấm, `eval/cham-run-3-de-xuat.csv`)* | 100% | 7/7 | 13/13 | 6/6 | **đạt**: `phong_dung_bang` 10/10 · `khong_noi_chot_khi_chua_chot` 8/8 · `hoi_lai_khi_thieu` 3/3 · `tu_choi_dung` 6/6 |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`, `eval/run-3.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`, `traces/run-3.jsonl`.

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

- Nhắm vào nhóm lỗi: **model trích ý sai** (điền rác vào trường, tự suy thông tin người dùng không nói, nhầm "kể" với "đòi") — vì sao đau nhất: làm trợ lý nói "không có buổi lab" khi có buổi (B08), mất một buổi chờ xác nhận (B19, B23), hoặc từ chối người đang cầm phòng cũ (B17): đúng kiểu đi nhầm phòng / bỏ buổi trong pain.
- Đã sửa gì (`codebase/agent.py`, chỉ bước ①): (1) chỉ nhận `buoi_lab` đúng dạng "LAB n"; (2) ca chỉ lấy khi người dùng tự nói "sáng" / "chiều", bỏ ca model tự suy; (3) prompt `SYSTEM_EXTRACT` ghi rõ người dùng kể phòng đã đổi rồi hỏi phòng đúng là `hoi_phong`, chỉ yêu cầu trợ lý làm gì mới là `doi_phong`.
- Kết quả: 4 câu của nhóm lỗi ở lượt 1 (B08, B17, B19, B23): 1 trượt + 2 thiếu buổi + 1 trượt → B17, B19, B23 đúng và đủ; **B08 vẫn trượt** vì nguyên nhân khác cùng nhóm: model tính "mai" = 02/05 (hôm nay) và ghi đè ngày code đọc được. Tổng 92% → 92%.
- Câu nào **tệ đi** sau khi sửa: **B05** ("Mai lab phòng nào?"): lượt 2 model tự đoán lớp = L3A nên trợ lý chỉ hỏi nhóm (lượt 1 hỏi đủ lớp + nhóm). Không do thay đổi của lượt 2 gây ra trực tiếp: cùng một lỗi "model đoán", lượt này rơi vào trường `lop` (model không ổn định giữa hai lượt).

## 4. Còn lại

- **Lượt 3 (thêm, cùng bộ câu thử, cùng cách chấm, không sửa lượt 1–2):** sửa tiếp cùng nhóm lỗi "model trích ý sai" theo một nguyên tắc: thông tin code đọc chắc được thì không để model đoán. (1) lớp / nhóm của model chỉ nhận khi có trong chữ người dùng gõ; (2) ngày tương đối ("mai", "hôm nay") do code tính, ưu tiên hơn ngày model suy. Kết quả: B05, B08 đạt → **26/26 (100%), đạt chuẩn §7**; không câu nào tệ đi (output các câu khác chỉ khác cách diễn đạt).
- Lỗi chưa sửa + nguy hiểm thế nào: model vẫn đọc ý định và các ngày dạng "thứ Năm" — model trả lời mỗi lượt một khác (lượt 1 đúng B05, lượt 2 sai), nên 26/26 ở một lượt chưa chứng minh ổn định. Bộ câu thử chỉ có 26 câu, nhiều câu nhóm tự viết; các cách sửa ở lượt 2–3 nhắm đúng lỗi thấy trong bộ này nên có nguy cơ khớp bộ câu thử hơn là khớp cách học viên thật gõ.
- Dữ liệu: bảng lịch là bộ giả lập BTC, danh sách nhóm tự dựng; chưa thử với bảng thật.
- Nếu có thêm 1 tuần: thay danh sách nhóm tự dựng bằng danh sách chính thức; chạy thêm câu thử theo đúng cách học viên gõ (lấy từ khảo sát / Discord); cho key coach thử duyệt bản nháp `draft_notice`.
