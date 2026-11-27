# AI SPEC — [Tên lát cắt] · Nhóm [tên nhóm] · Phòng [XXX] · Zone [X]

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [ ] A · [ ] B · [ ] C · [ ] D · [ ] E — bài toán: [đề gợi ý trong file track, hoặc bài toán nhóm tự mở rộng] __
Data BTC cấp đã dùng (nếu có — không commit nguyên file): __

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại của việc này, trong khoá hoặc trên app thật (3–5 bước; ảnh chụp từ tài khoản của mình, đã che thông tin):
- Công cụ / AI đang được dùng cho việc này (nếu có) + nguồn. Không kiểm được thì ghi "chưa kiểm":

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính (một vai cụ thể):
- Việc họ cố làm xong (`động từ + đối tượng + bối cảnh`, không có chữ AI):
- Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ:
- Pain (KHÔNG chữ AI): ai — đang làm gì — vướng đâu — hậu quả gì:
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/summary.md`): __

## §2. Impact & quyết định chọn *(guide 1.3)*

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

- **Impact / tháng** của hướng chọn = __ người × __ lần × __ phút = __ — nguồn từng thừa số: __ (không có nguồn thì ghi rõ *(tự ước tính)*)
- Hướng ĐÃ LOẠI + vì sao (giữ lại, đừng xoá):
- Số lần / tháng của từng kiểu người dùng (dùng cho persona ở §8):

## §3. Giải pháp tương tự *(guide 2.1)*
- [sản phẩm / tính năng gần giống]: một điều đáng học · một điều đáng né · mình khác gì

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả):
- Không làm (≥3 điều):
- **Sơ đồ** (ảnh / Mermaid / draw.io): [chèn ở đây]
- **Hình dạng:** [ ] workflow cố định · [ ] một agent · [ ] nhiều agent — 2 dòng lý do, và vì sao **không** chọn hình dạng phức tạp hơn:
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  |  |  |  |  |

- **Mức tự động:** [ ] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — lý do (sai thì ai chịu gì, sửa đắt hay rẻ):
- **Chỗ chặn rủi ro** (rủi ro lớn nhất của lát cắt bị chặn ở đâu, bằng gì):
- **Chỗ người duyệt** (việc AI không được tự làm):
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc |  |
  |  |  |
  |  |  |

- Phần nào còn giả (công cụ trả dữ liệu giả, model chế độ giả…) — ghi rõ, không giả làm thật:

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
|  |  |  |  |
| *(tấn công)* |  |  |  |
| *(tấn công)* |  |  |  |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- Mọi thứ suôn sẻ: · Không chắc (lớp 2): · Không có căn cứ (lớp 1): · Người dùng sửa:
- Bị đòi ngoài phạm vi (lớp 3): · Trường hợp đặc thù lĩnh vực (lớp 4):

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` — __ câu (thuong __ · kho __ · tu_choi __) · metric: `eval/metric_spec.yaml` (__ metric)
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): "Đạt khi ≥ __% câu qua, và __"
- Kết quả: lượt 1 __/__ (__%) · lượt 2 __/__ (__%) — run ID: __ / __ → chi tiết `eval/report.md`, hồ sơ `eval/README.md`

## §8. Chi phí khi dùng thật *(guide 4.2)*
- Persona + giá: `cost/personas.yaml` · lượt mô phỏng: `cost/simulate-__.csv` (__ phiên)
- Chi phí / task thành công: __ (model __) · __ (model __)
- Chi phí / tháng ở quy mô thật: thấp __ · cơ sở __ · cao __ → chi tiết `cost/cost-estimate.md`
- So với impact / người / tháng (§2): đáng làm không, vì sao:

## §9. Rủi ro & an toàn
- Dữ liệu: đã ẩn danh gì, không thu gì, không đưa gì vào model gói miễn phí:
- AI **không được** làm gì kể cả khi người dùng yêu cầu:
- Ai có thể bị hại nếu AI sai, và nhóm chặn thế nào:

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp — guide "Cách chia việc"): mỗi người **giữ một mảng** và phải giải thích được phần có tên mình; **cặp đổi sau CP2** để ai cũng kể lại được cả câu chuyện; ai cũng tự chạy `run.py eval` và `run.py simulate` ít nhất một lần.
  - **Đỗ Nhật Anh** (đội trưởng): bản chạy thử `codebase/` (luồng, công cụ, nối model, chặn rủi ro) · §9–§10 · nộp checkpoint
  - **Phạm Cát Tân:** bằng chứng pain và impact — `evidence/` · §0–§2 · slide
  - **Vũ Đức Anh:** bộ câu thử và đánh giá — `eval/` · `data/DATA_CARD.md` · §5–§7
  - **Trần Thái Hưng:** thiết kế và chi phí — §3–§4 · §8 · data chạy thử trong `data/` · `cost/`

  | Chặng · mốc | Cả nhóm | Cặp 1 | Cặp 2 |
  |---|---|---|---|
  | **1 · đến 17:00 T6 (CP1)** | Mỗi người phỏng vấn ≥1 học viên ngoài nhóm về lần gần nhất kẹt khi xem video pre-class → `evidence/interviews/P*.md` · 16:45 đi lại câu chuyện | **Nhật Anh:** push repo, nộp CP1, hỏi lab coach nghĩa của `missing_context`, `by = link` · **Thái Hưng:** xem 2–3 video Day01–02, tự viết lại thành 10–20 đoạn ngắn có mốc giây (không chép nguyên lời giảng) | **Đức Anh:** đọc `eval/README.md`, `metric_spec.yaml`; hỏi tay 10 câu bằng ChatGPT/Claude với prompt nháp, ghi output để viết tiêu chí · **Cát Tân:** chuẩn bị khung tổng hợp phỏng vấn |
  | **3 · 17:00–19:30 T6 (CP2)** | 17:00–17:20 tổng hợp phỏng vấn (Cát Tân dẫn) → chốt lát cắt + sơ đồ · 19:00 đổi chéo review · **19:15 chốt §7 chuẩn "đạt"**, commit trước 19:30 · Nhật Anh nộp CP2 | **Nhật Anh + Thái Hưng:** sơ đồ §4 + data chạy thử (Thái Hưng) · `tools.py` `search_lesson` + `agent.py` đi hết luồng với AI giả (Nhật Anh) · trước khi rời lớp: lấy API key, `run.py eval --try` | **Đức Anh + Cát Tân:** §5 ≥6 kịch bản + 2 tấn công · `benchmark.csv` ≥10 câu · `metric_spec.yaml` ≥3 metric · `DATA_CARD.md` (Đức Anh) · canvas + dòng "đã đổi gì" · §1 (Cát Tân) · hai người chấm độc lập cùng 5 output, ghi `eval/README.md` |
  | **4 · tối T6 → 10:00 T7 (CP3)** | Sáng T7 30 phút: chốt bằng chứng + impact · chạy `run.py eval` lượt 1 cùng nhau, chấm `pass`, `score` · 09:45 đi lại câu chuyện · Nhật Anh quay video 30 giây, nộp CP3 | **Nhật Anh + Đức Anh:** nối model thật `ai.py` + code chặn mốc giây không có trong kết quả công cụ (Nhật Anh) · mở rộng 20–30 câu thử: ≥5 `kho`, ≥2 `tu_choi` gồm 2 tấn công, ≥1/3 từ người dùng / data thật (Đức Anh) | **Cát Tân + Thái Hưng:** `evidence/summary.md`, §0 hiện trạng trợ giảng, bảng impact §2 ≥3 hướng (Cát Tân) · §3 giải pháp tương tự, `cost/personas.yaml`, `run.py simulate --try` 10 phiên (Thái Hưng) |
  | **5 · 10:00–13:00 T7** | 30 phút đọc chung các câu trượt → gom nhóm lỗi → chọn 1 cải tiến · *(bonus)* mỗi người cho 1 người ngoài nhóm dùng thử → `validation/log.md` | **Nhật Anh + Đức Anh:** cải tiến → `run.py eval` lượt 2 (Nhật Anh) · `eval/report.md` + `eval/README.md` (Đức Anh) | **Cát Tân + Thái Hưng:** `run.py simulate` ≥50 phiên với tỉ lệ đạt lượt 2 · `cost/cost-estimate.md` 3 kịch bản × 2 model, giá có link + ngày xem (Thái Hưng) · cập nhật số §1–§2, bắt đầu slide (Cát Tân) |
  | **6 · 13:00–14:30 T7 (CP4)** | Go / iterate / stop · tập demo, mỗi người nói một phần: Cát Tân (pain + impact) · Thái Hưng (giải pháp + chi phí) · Đức Anh (đánh giá) · Nhật Anh (demo live) · 14:15 đi lại câu chuyện · Nhật Anh nộp CP4 | **Nhật Anh + Đức Anh:** video demo dự phòng · checklist 5.2 (không có key, không có dữ liệu cá nhân) · §9 | **Cát Tân + Thái Hưng:** slide 8 trang (`slides/outline.md` → PDF) · §8 |
  | **14:30 → 23:59 T7** | Mỗi người một file `reflection/<ten-khong-dau>.md` · sửa theo góp ý | **Nhật Anh:** ghi changelog §10 cho mọi thay đổi sau 14:30 | |
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`):
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
|  |  |  |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
