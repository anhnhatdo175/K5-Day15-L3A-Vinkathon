# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | | | | |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, gợi ý nhãn) | Claude Code | Thêm M12 vào `evidence/count_preclass.py`; đếm hình dạng bộ lịch giả lập `data/training-ops/` (chỉ để hiểu workflow, không làm bằng chứng) | Chạy lại `python evidence/count_preclass.py` ra đúng số ở `evidence/data-mining.md` · người kiểm: __ | Nhật Anh |
| Rà câu hỏi phỏng vấn / khảo sát | Claude Code | Soạn `evidence/interviews/GUIDE-A5.md`, `evidence/survey/questions.md`: chỉ hỏi chuyện đã xảy ra trong 1 tháng qua | Rà câu dẫn dắt · người kiểm: __ | Nhật Anh |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | Claude Code | Soạn nháp canvas, `evidence/hypothesis.md`, `spec.md` (header, §0–§2, §10), README, TEAMS (cột phần việc) cho hướng A5 | Đọc lại, sửa trước khi commit · người kiểm: __ | Nhật Anh |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
