# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | | | | |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, gợi ý nhãn) | Claude Code | Thêm M12 vào `evidence/count_preclass.py`; đếm hình dạng bộ lịch giả lập `data/training-ops/` (chỉ để hiểu workflow, không làm bằng chứng) | Chạy lại `python evidence/count_preclass.py` ra đúng số ở `evidence/data-mining.md` · người kiểm: __ | Nhật Anh |
| Rà câu hỏi phỏng vấn / khảo sát | Claude Code | Soạn `evidence/interviews/GUIDE-A5.md`, `evidence/survey/questions.md`: chỉ hỏi chuyện đã xảy ra trong 1 tháng qua | Rà câu dẫn dắt · người kiểm: __ | Nhật Anh |
| Viết câu thử (benchmark) | Claude Code | 27/11 ~19:10: thêm B17–B20 từ ghi chép phỏng vấn P1–P5 (cột `source` trỏ về P_), sửa `pass_criterion` B01–B04, B10–B12; sửa định nghĩa 4 metric trong `eval/metric_spec.yaml`; soạn 5 output chấm thử + bảng mẫu tự dựng `eval/calibration-5.md` (ghi rõ không phải output bản chạy thử); soạn nháp spec §5–§7, `data/DATA_CARD.md`; ~19:20: gộp hai cột chấm do người điền vào phiếu, đếm khớp, viết lại định nghĩa 3 metric theo chỗ lệch (AI không chấm, không điền điểm) | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ · phiếu chấm 5 output do người chấm, AI không điền · người kiểm: __ | Đức Anh |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | Claude Code | Soạn nháp canvas, `evidence/hypothesis.md`, `spec.md` (header, §0–§2, §10), README, TEAMS (cột phần việc) cho hướng A5; 27/11 ~19:10: tóm số từ P1–P5 vào spec §1 + canvas dòng 4 và dòng "Đã đổi gì" (chỉ chép số / trích dẫn có trong file phỏng vấn) | Đọc lại, sửa trước khi commit · người kiểm: __ | Nhật Anh |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
