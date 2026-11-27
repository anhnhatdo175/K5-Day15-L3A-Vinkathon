# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Repo chỉ chứa số đã tổng hợp và vài dòng ví dụ — không chép lại nguyên file data.

**Chạy lại:** chép `data/preclass/` của repo đề vào `data-btc/preclass/` (đã có trong `.gitignore`, không commit), rồi
`python evidence/count_preclass.py`: chỉ dùng thư viện chuẩn, ra đúng các số ở mục 3.

## 1. Cách đếm

> **Ghi chú trung thực về thứ tự:** nhóm đào thử data một lượt trước (27/11 sáng, để chọn hướng), rồi mới chốt định nghĩa dưới đây và viết lại thành `evidence/count_preclass.py`. Các định nghĩa không đổi sau khi chốt.

- **Data dùng:** `data/preclass/` do BTC cấp (đã ẩn danh), `events.csv` (107.709 dòng) và `chat.csv` (1.260 dòng), từ 05/11/2026 đến 25/11/2026. Giờ trong data là UTC, đổi sang giờ Việt Nam bằng +7.
- **Tập học viên:** 721 tài khoản, **436 học viên có hoạt động** (≥1 sự kiện `actor = learner`), **431 học viên có mở video**. Mẫu số chọn theo từng số, ghi rõ ở bảng.

| Mã | Đếm gì | Mẫu số |
|---|---|---|
| M1 | cặp (học viên, video) có ≥1 `video_ended` | cặp (học viên, video) có ≥1 `video_opened` |
| M2 | học viên có ≥1 `video_seeked` với `to < from` (tua lui) | học viên có mở video |
| M3 | học viên có ≥1 `video_opened` lúc 22:00–01:59 giờ VN | học viên có mở video |
| M4 | học viên có ≥1 dòng `chat.csv` với `addressed_agent_id = teaching_assistant` | học viên có hoạt động |
| M5 | câu trả lời của trợ giảng (`agent_replied` nối `chat.csv` có `addressed_agent_id = teaching_assistant`) có `moc_trich_dan` khác rỗng | câu trả lời của trợ giảng có ghi khoá `moc_trich_dan` (khoá này chỉ có từ 13/11) |
| M6 | `video_seeked` có `by = link`; trong đó bao nhiêu lần xảy ra trong 10 phút sau một câu trả lời của trợ giảng cho chính học viên đó | - (đếm số lần, số học viên) |
| M7 | câu trả lời của trợ giảng có `missing_context = true` | câu trả lời của trợ giảng có ghi khoá này |
| M8 | câu hỏi gửi trợ giảng có `do_dai_cau_hoi ≤ 10` ký tự | câu hỏi gửi trợ giảng |
| M9 | học viên chạm Day01 (theo `lesson_id`) có chạm Day08 | học viên chạm Day01 |
| M10 | cặp (học viên, `intervention_id`) mà học viên đó có ≥1 dòng `chat.csv` trả lời đúng `intervention_id` | cặp (học viên, `intervention_id`) từ `agent_message_shown` có `intervention_id` |
| M11 | `lab_completed` có `skipped = true` | mọi `lab_completed` |

## 2. Đọc trước, đếm sau

Đã đọc README của data, `column_dictionary.csv`, `event_types.csv` và các dòng đầu của từng file. Các *kiểu* hành vi thấy được:
- Xem video: mở, tua tới / tua lui, xem tới cuối, rời tab; câu hỏi bật lên giữa video.
- Hỏi AI: nhắn trợ giảng dưới video, bôi đen chữ trên slide để hỏi, nhắn trong khung thảo luận với bạn học AI.
- Bạn học AI tự xen vào bài giảng (do bộ điều phối quyết định); học viên có thể trả lời lại.
- Mini lab: mở, làm xong, hoặc bấm bỏ qua. Sổ hiểu bài: rất ít dùng (51 học viên mở).

## 3. Kết quả

| Mã | Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|---|
| M1 | Cặp (học viên, video) xem tới cuối | 1.676 / 3.900 | 43% | Thấp nhất ở video Day01: 244/922 (26%) |
| M2 | Học viên từng tua lui | 177 / 431 | 41% | |
| M3 | Học viên từng mở video lúc 22h–02h | 168 / 431 | 39% | 23,6% lượt mở video (1.710/7.254) rơi vào khung này |
| M4 | Học viên từng nhắn trợ giảng AI | 143 / 436 | 33% | |
| M5 | Câu trả lời của trợ giảng **có** mốc trích dẫn | 327 / 558 | 59% | **Hiện trạng:** trợ giảng đang có đã trích mốc giây ở đa số câu (từ 13/11) |
| M6 | Lần tua bằng `link` | 40 lần · 15 học viên | - | 22/40 lần trong 10 phút sau một câu trả lời của trợ giảng |
| M7 | Câu trả lời của trợ giảng có `missing_context = true` | 99 / 1.081 | 9% | Nghĩa của cờ chưa được mô tả, xem mục 5 |
| M8 | Câu hỏi gửi trợ giảng ≤10 ký tự | 70 / 1.096 | 6% | |
| M9 | Học viên Day01 còn chạm Day08 | 107 / 417 | 26% | Dùng cho bảng so sánh hướng (`spec.md` §2) |
| M10 | Lượt bạn học AI xen vào được học viên trả lời | 89 / 7.992 | 1,1% | 273 học viên thấy lời xen vào, 31 học viên từng trả lời. Hướng A4 |
| M11 | Lần xong mini lab là bấm "bỏ qua" | 102 / 453 | 23% | Hướng A6 |

## 4. Ví dụ cụ thể (mã đã ẩn danh: không đoán ai là ai)

Chọn theo thứ tự mã đầu tiên thoả điều kiện (không chọn theo xếp hạng), in ra bởi `count_preclass.py`:

1. Học viên `L0093` · video `d04-r3-v01`: mở 3 lần, tua lui 9 lần, không có `video_ended`.
2. Lượt chat `C00021`: câu hỏi gửi trợ giảng dài 9 ký tự; trợ giảng trả lời 548 ký tự (video `Day03/d03-r2-v03`).
3. Lượt chat `C00002`: trợ giảng trả lời 583 ký tự, không kèm mốc trích dẫn nào (`moc_trich_dan = []`).
4. Lượt chat `C00014`: câu trả lời có `missing_context = true`, dài 161 ký tự (câu hỏi 75 ký tự).
5. Học viên `L0181`: tua bằng `link` lúc 16/11 10:41, trong 10 phút sau một câu trả lời của trợ giảng.

## 5. Giới hạn của data

- Data cho biết người ta **làm gì**, không cho biết **vì sao**: xem dở có thể do kẹt nội dung, cũng có thể do hết giờ; tua lui có thể do không hiểu, cũng có thể do xem lại cho chắc.
- **Không có chữ học viên viết và chữ AI trả lời** (chỉ có độ dài) → không biết câu hỏi hỏi gì, không chấm được câu trả lời của trợ giảng đúng hay sai, mốc trích dẫn có đúng đoạn không.
- `missing_context` và `by = link` **không có định nghĩa** trong `column_dictionary.csv` / `event_types.csv`. Nhóm đoán: `missing_context` = trợ giảng thiếu căn cứ trong bài để trả lời; `link` = tua do bấm một đường dẫn (có thể là mốc giây trong câu trả lời). **Chưa kiểm, cần hỏi BTC** trước khi dùng hai số này làm bằng chứng chính.
- `moc_trich_dan` chỉ được ghi từ 13/11 → không biết trước đó trợ giảng có trích mốc không.
- `video_ended` có thể bật cả khi học viên tua tới cuối → M1 có thể **cao hơn** số người thật sự xem hết.
- Mẫu chỉ gồm học viên có dùng trang pre-class (436/721 tài khoản); người không dùng không có trong data. Day10–Day13 ít người một phần vì bài mở muộn.
- Không so `maic` với `tutor` (chế độ học chỉ ghi từ 25/11, README data dặn không so).

→ **Kiểm lại bằng phỏng vấn ≥3 học viên ngoài nhóm** (`evidence/interviews/P1.md`…): lần gần nhất kẹt khi xem video pre-class đã làm gì, mất bao lâu · có hỏi trợ giảng không, vì sao có / không · khi được chỉ ra đoạn bài thì có mở lại không · vì sao không xem hết video.
