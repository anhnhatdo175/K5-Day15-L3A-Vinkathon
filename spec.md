# AI SPEC — Trợ lý phòng lab có căn cứ · Nhóm Vinkathon · Phòng __ · Zone __

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [x] A · [ ] B · [ ] C · [ ] D · [ ] E — bài toán: **A5 · Vận hành đào tạo** (đề gợi ý trong file track A): học viên L3 cần biết chắc phòng và giờ của buổi lab, trong khi phòng chỉ chốt sát ngày và thông tin nằm ở nhiều nơi
Data BTC cấp đã dùng (nếu có — không commit nguyên file): `data/training-ops/` (**giả lập**, chỉ để hình dung workflow và dựng bản chạy thử, không phải bằng chứng pain; nguyên file để ở `data-btc/`, không commit) · `data/preclass/` (số cho các hướng so sánh ở §2)

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại của việc này (nguồn: file track A, mục A5 "Hiện trạng" do BTC mô tả; cấu trúc bảng: `data/training-ops/README.md`):
  1. Ban đào tạo gom form đăng ký của giảng viên vào **một bảng lịch chung**, mỗi ô là chữ tự do (lớp, chủ đề, phòng, giảng viên). Lớp L3 hơn 700 học viên, chia L3A và L3B; mỗi buổi lab rải 3–6 phòng ở nhiều khu.
  2. **Nhiều phòng chỉ chốt sát ngày học**, có khi ngay trong ngày, và vẫn có thể đổi; tới lúc chốt, ô lịch ghi "Phòng dự kiến … (chờ xác nhận)" hoặc "Phòng: chờ xác nhận".
  3. Đội lab coach giữ **bảng riêng** (chép lịch từ bảng chung), đổi ca qua form và nhóm Zalo.
  4. Học viên **nhận lịch qua email**, tra nhóm của mình trong **một link danh sách**; ai chưa chắc thì hỏi trên Discord, Zalo, hỏi bạn hoặc coach *(phần hỏi: giả thuyết, kiểm bằng phỏng vấn)*.
  - Ảnh chụp từ tài khoản của mình: **chưa có**; chụp email lịch lab và danh sách nhóm gần nhất của chính mình (che thông tin) trước CP3.
  - Hình dạng vấn đề trong bộ **giả lập** của BTC (chỉ để hình dung, **không phải bằng chứng**): lúc xuất bảng phân công 27/04/2027 21:00, 22/43 ô buổi chưa học còn chưa chốt phòng; bản chép lịch trong file lab coach lệch dòng phòng ở 44/133 ô so với bảng gốc; buổi L3B LAB 10 có ba nơi ghi ba giá trị phòng khác nhau.
- Công cụ / AI đang được dùng cho việc này (nếu có) + nguồn: **chưa kiểm**; hỏi trong phỏng vấn: có bot / kênh nào trả lời phòng, lịch không, ai trả lời các câu "phòng nào" hiện nay.

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính (một vai cụ thể): **học viên lớp L3 (L3A / L3B) khoá AI20K đi lab trực tiếp**, tối trước buổi lab mới đi tìm phòng của nhóm mình.
- Việc họ cố làm xong (`động từ + đối tượng + bối cảnh`, không có chữ AI): **biết chắc phòng và giờ của buổi lab sắp tới của nhóm mình, trước khi đến trường.**
- Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ *(giả thuyết, kiểm bằng phỏng vấn, khảo sát)*: đọc email lịch, tra nhóm trong link danh sách, hỏi trên Discord / Zalo / hỏi bạn. Hỏng khi phòng chưa chốt lúc gửi lịch, đổi sau khi đã báo, hoặc các nơi ghi khác nhau. Chưa bỏ vì không có nơi nào chính thức hơn để tra.
- Pain (KHÔNG chữ AI): **học viên L3 tối trước buổi lab tìm xem nhóm mình học phòng nào, mấy giờ, nhưng phòng còn "chờ xác nhận" hoặc đổi sau khi đã báo, thông tin ở email, danh sách nhóm, Discord, Zalo không khớp nhau, nên phải hỏi đi hỏi lại, đến trễ hoặc đi nhầm phòng, mất đầu giờ lab.**
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/summary.md`): **chưa có, đang thu** (khảo sát ≥20 + phỏng vấn ≥3 từ 27/11 17:40). Giả thuyết và ngưỡng "đúng / sai": `evidence/hypothesis.md`.

## §2. Impact & quyết định chọn *(guide 1.3)*

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| **A5 · học viên biết chắc phòng / giờ buổi lab** | >700 học viên L3 (file track A, mục A5) × __% từng gặp sự cố phòng lab trong tháng (khảo sát câu 5–6) | __ buổi lab / người / tháng (khảo sát câu 2) × __ lần gặp sự cố (khảo sát câu 5–6) | __ phút mỗi lần (khảo sát câu 7), trễ đầu giờ lab | __ *(chờ khảo sát)* | Kịp: một quyết định AI; bảng lịch giả lập của BTC có sẵn để chạy thử | ✅ Chọn |
| A5 · key coach soạn và báo phòng mỗi tối trước buổi lab | __ key coach / Day Lead (phỏng vấn) | __ tối / tháng (phỏng vấn) | __ phút / tối (phỏng vấn) | __ | Kịp, nhưng phải tự dựng danh sách nhóm; key coach ít người, khó đủ 3 người phỏng vấn | Dự phòng |
| A4 · lớp học kiểu mới (bạn học AI xen vào bài giảng) | 273 học viên thấy lời bạn học AI xen vào, 31 từng trả lời (M10, `evidence/data-mining.md`) | 89/7.992 lượt xen vào được học viên trả lời (1,1%, 05/11–25/11) | Chưa đo được: data không có chữ, không biết vì sao không trả lời | - | Sản phẩm lớn; chuẩn "đạt" phải có chỉ số về học | ❌ Loại |
| A6 · hỗ trợ mini lab | 453 lần làm xong mini lab (M11) | 102/453 lần là bấm "bỏ qua" (23%, M11) | Chưa biết vì sao bỏ qua | - | Phải tự thu mọi dữ liệu | ❌ Loại |

- **Impact / tháng** của hướng chọn = __ học viên × __ lần × __ phút = __ — nguồn từng thừa số: số học viên = >700 học viên L3 (file track A, mục A5) × tỉ lệ từng gặp sự cố (khảo sát câu 5–6) · số lần / tháng = khảo sát câu 2, 5, 6 · phút mỗi lần = khảo sát câu 7 *(chưa có số, điền trước CP3; thừa số nào không có nguồn thì ghi rõ (tự ước tính))*
- Hướng ĐÃ LOẠI + vì sao (giữ lại, đừng xoá):
  - **A4:** chỉ 1,1% lượt bạn học AI xen vào được trả lời, nhưng data không cho biết vì sao; làm cần đo "học được" (chỉ số về học), quá to cho khoảng 10 giờ.
  - **A6:** 23% lần xong mini lab là bấm bỏ qua, nhưng chưa biết vì sao bỏ qua; hướng riêng phải tự thu mọi dữ liệu.
  - **A5 phía key coach:** giữ làm **dự phòng**: chọn nếu phỏng vấn cho thấy chỗ đau nằm ở phía coach và gặp đủ ≥3 key coach / Day Lead.
- Số lần / tháng của từng kiểu người dùng (dùng cho persona ở §8): chờ khảo sát câu 2 và câu 8; dự kiến 3 kiểu: hỏi dồn tối trước buổi lab · hỏi rải rác · không hỏi (chỉ xem email).

## §3. Giải pháp tương tự *(guide 2.1)*
- [sản phẩm / tính năng gần giống]: một điều đáng học · một điều đáng né · mình khác gì

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả): một học viên L3 · tối trước buổi lab hỏi "mai lab phòng nào" · trợ lý quyết định **nêu phòng** (chỉ khi phòng đã chốt trong bảng phân công mới nhất, kèm giờ cập nhật bảng), **hỏi lại một câu** khi thiếu lớp / ngày / nhóm, hay **nói "phòng chưa chốt"** và soạn câu hỏi chuyển key coach · học viên biết chắc phòng, hoặc biết là phòng chưa chốt, nên không đi nhầm.
- Không làm:
  1. Không chốt, không đổi, không gợi ý phòng (phòng do trường cấp).
  2. Không tự gửi thông báo hay tin nhắn cho ai; câu hỏi cho key coach chỉ là **bản nháp chờ duyệt**.
  3. Không giúp key coach / ban đào tạo chia coach theo phòng (lát cắt khác của A5).
  4. Không trả lời lịch buổi giảng, điểm danh, nội dung bài lab; chỉ phòng + giờ buổi lab L3A / L3B.
  5. Không đọc Discord / Zalo / email làm nguồn; chỉ bảng phân công chính thức (và bảng lab coach để **phát hiện lệch**, không để trả lời).
- **Sơ đồ** (Input → AI Core → Chặn rủi ro → Output):

  ```mermaid
  flowchart TD
      IN["INPUT<br/>Câu học viên L3 gõ<br/>vd 'mai L3A nhóm 7 lab phòng nào?'"]

      subgraph CORE["AI CORE · workflow cố định"]
          P["① Trích ý (model)<br/>lớp · ngày · nhóm / tên"]
          V{"② Đủ lớp + ngày + nhóm?<br/>(code)"}
          T1["③ get_schedule(date, class)<br/>bảng phân công chính thức mới nhất<br/>→ buổi · giờ · phòng · trạng thái · giờ cập nhật"]
          T2["④ find_group(class, query)<br/>danh sách nhóm chuẩn<br/>→ nhóm của học viên"]
          C["⑤ check_conflicts(plan) (code)<br/>so bảng chính thức với bảng lab coach<br/>→ chốt / chờ xác nhận / online / lệch / không có buổi"]
          W["⑥ Viết câu trả lời (model)<br/>chỉ từ dữ kiện ③–⑤"]
      end

      subgraph GUARD["CHẶN RỦI RO · code, không tin model"]
          G1{"⑦ Mã phòng + giờ trong câu trả lời<br/>có đúng trong kết quả ③ không?"}
          G2{"⑧ Trạng thái 'chốt'?"}
          D["draft_notice(class, changes)<br/>NHÁP câu hỏi cho key coach<br/>trạng thái: chờ duyệt, không tự gửi"]
      end

      O1["OUTPUT · Phòng X, giờ Y<br/>theo bảng cập nhật lúc HH:MM"]
      O2["OUTPUT · Hỏi lại 1 câu<br/>(thiếu lớp / ngày / nhóm, tên lệch danh sách)"]
      O3["OUTPUT · 'Phòng chưa chốt' / 'buổi chuyển online' /<br/>'các bảng đang ghi khác nhau'<br/>+ đã soạn câu hỏi cho key coach"]
      KC(["Key coach duyệt rồi mới gửi"])

      IN --> P --> V
      V -- thiếu --> O2
      V -- đủ --> T1 --> T2 --> C --> W --> G1
      T2 -- không tìm thấy / nhiều kết quả --> O2
      G1 -- sai / bịa --> O3
      G1 -- đúng --> G2
      G2 -- chốt --> O1
      G2 -- chờ xác nhận / lệch / online --> D --> O3
      D -.-> KC
  ```

- **Hình dạng:** [x] workflow cố định · [ ] một agent · [ ] nhiều agent. Lý do: các bước luôn giống nhau (trích ý → tra bảng → so lệch → trả lời), nên không cần AI tự chọn bước. Model chỉ ở hai chỗ, ① trích ý và ⑥ viết câu; tra bảng, so lệch và kiểm phòng chạy bằng code. **Không chọn agent** vì sai phòng thì học viên đi nhầm, mà agent tự chọn công cụ khó kiểm lại và khó chặn. Không cần nhiều agent vì chỉ có một việc, một người dùng.
- **AI dựa vào đâu** — mỗi công cụ (đề xuất; Cát Tân khớp tên khi viết `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  | `get_schedule` | `date` (YYYY-MM-DD), `class` (L3A / L3B) | danh sách buổi lab trong ngày: mã buổi, giờ bắt đầu–kết thúc, phòng theo nhóm, trạng thái phòng (`chot` / `cho_xac_nhan` / `online`), giờ cập nhật bảng | Không (chỉ đọc) |
  | `find_group` | `class`, chuỗi học viên gõ (số nhóm hoặc tên) | nhóm khớp trong danh sách chuẩn; 0 hoặc >1 kết quả thì trả rỗng / danh sách để hỏi lại | Không (chỉ đọc) |
  | `check_conflicts` | kết quả `get_schedule` + bảng lab coach cùng buổi | các chỗ lệch phòng / giờ / trùng phòng giữa hai bảng; **chạy bằng code, không phải AI** | Không (chỉ đọc) |
  | `draft_notice` | `class`, `changes` (buổi, nhóm, vấn đề: chưa chốt / lệch / online) | bản nháp câu hỏi cho key coach, trạng thái `cho_duyet` | **Không gửi**; chỉ tạo nháp, key coach duyệt rồi tự gửi |

- **Mức tự động:** [ ] AI gợi ý, người quyết · [x] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm. Lý do: câu "phòng nào" nhiều, lặp lại; khi bảng đã chốt thì trả lời ngay là rẻ và đúng. Sai thì học viên đi nhầm phòng, trễ đầu buổi lab, đến nơi mới biết thì sửa đắt, nên mọi trường hợp chưa chắc (chưa chốt, hai bảng lệch, chuyển online, không tìm thấy nhóm) đều không đoán mà nói rõ + chuyển key coach.
- **Chỗ chặn rủi ro:** rủi ro lớn nhất là **nêu sai phòng hoặc nêu phòng "chờ xác nhận" như đã chốt**. Chặn ở ⑦–⑧ bằng code: tách mã phòng và giờ trong câu trả lời của model, so với kết quả `get_schedule` của đúng buổi, đúng nhóm; không khớp thì bỏ câu của model, trả câu mẫu "chưa xác định được phòng" + nháp cho key coach. Trạng thái khác `chot` thì không bao giờ ra nhánh O1.
- **Chỗ người duyệt:** mọi thông báo / câu hỏi gửi cho key coach, coach hay học viên khác (`draft_notice` chỉ tạo nháp); việc chốt hoặc đổi phòng; xử lý khi hai bảng lệch nhau.
- **Nguyên tắc thiết kế:**

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc | ② thiếu lớp / ngày / nhóm → hỏi lại đúng một câu; ⑧ phòng chưa chốt, lệch hay online → chỉ nói tình trạng, không đoán phòng (nhánh O2, O3) |
  | Một nguồn sự thật | ③ chỉ bảng phân công chính thức mới nhất được dùng để trả lời; bảng lab coach chỉ vào ⑤ để phát hiện lệch |
  | Code kiểm, không tin model | ⑦ mã phòng + giờ trong output phải có trong kết quả công cụ; ⑤ so lệch chạy bằng code |
  | Cho người dùng biết độ mới của thông tin | O1 luôn kèm "theo bảng cập nhật lúc HH:MM" để học viên biết khi nào nên hỏi lại |
  | Tác động ra ngoài chỉ là nháp | `draft_notice` trả trạng thái `cho_duyet`, không có hàm gửi |

- Phần nào còn giả: **model đang ở chế độ giả** (`MODEL_PROVIDER=fake`) đến khi nối API key; **dữ liệu lịch là bộ giả lập của BTC** (`data/training-ops/`, không phải lịch thật); `draft_notice` không nối kênh gửi nào (cố ý, không phải chưa làm); tên công cụ ở bảng trên là đề xuất, cập nhật theo `codebase/tools.py` khi Cát Tân viết xong.

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
- Phân công có tên (theo chặng, chia cặp, guide "Cách chia việc"): mỗi người **giữ một mảng** và phải giải thích được phần có tên mình; **cặp đổi sau CP2** để ai cũng kể lại được cả câu chuyện; ai cũng tự chạy `run.py eval` và `run.py simulate` ít nhất một lần.
  - **Đỗ Nhật Anh** (đội trưởng): bằng chứng pain và impact, `evidence/` (khảo sát + phỏng vấn học viên L3 về phòng lab) · §0–§2 · slide · §10 · nộp checkpoint
  - **Phạm Cát Tân:** bản chạy thử `codebase/` (tra bảng lịch, kiểm mã phòng, nối model, chặn rủi ro) · §9
  - **Vũ Đức Anh:** bộ câu thử và đánh giá, `eval/` · `data/DATA_CARD.md` · §5–§7
  - **Trần Thái Hưng:** thiết kế và chi phí, §3–§4 · §8 · data lịch chạy thử trong `data/` (tách từ bảng giả lập `training-ops`) · `cost/`

  | Chặng · mốc | Cả nhóm | Cặp 1 | Cặp 2 |
  |---|---|---|---|
  | **1 · đến 17:00 T6 (CP1)** | Chọn track A, hướng A5 · giả thuyết `evidence/hypothesis.md` (commit **trước** khi hỏi ai) · canvas 7 dòng · bộ câu phỏng vấn `evidence/interviews/GUIDE-A5.md` + khảo sát `evidence/survey/questions.md` | **Cát Tân:** đọc `codebase/` (`agent.py`, `tools.py`, `ai.py`) + `docs/connect-model.md`, chạy `python run.py` ở chế độ giả để nắm khung trước chặng 3 · **Thái Hưng:** đọc `data/training-ops/` (README + 2 file xlsx), ghi lại các kiểu ô lịch: phòng đã chốt, "dự kiến", "chờ xác nhận", online, giờ riêng, nghỉ lễ | **Đức Anh:** đọc `eval/README.md`, `metric_spec.yaml`; hỏi tay 10 câu về phòng / giờ lab bằng ChatGPT/Claude kèm bảng lịch giả lập, ghi output để viết tiêu chí · **Nhật Anh:** push repo, nộp CP1, gửi khảo sát vào nhóm lớp, hỏi lab coach zone ai đang làm key coach / Day Lead để hẹn phỏng vấn |
  | **3 · 17:00–19:30 T6 (CP2)** | Mỗi người phỏng vấn ≥1 học viên L3 ngoài nhóm về buổi lab gần nhất (`GUIDE-A5.md` → `evidence/interviews/P*.md`) + cố gặp 1–2 lab coach / key coach đang ở lớp · 18:30 tổng hợp phỏng vấn + khảo sát (Nhật Anh dẫn) → chốt người dùng, lát cắt, sơ đồ · 19:00 đổi chéo review · **19:15 chốt §7 chuẩn "đạt"**, commit trước 19:30 · Nhật Anh nộp CP2 | **Cát Tân + Thái Hưng:** sơ đồ §4 + tách bảng lịch giả lập thành data chạy thử trong `data/` (Thái Hưng) · `tools.py` tra buổi theo ngày / lớp + `agent.py` đi hết luồng với AI giả (Cát Tân) · trước khi rời lớp: lấy API key, `run.py eval --try` | **Đức Anh + Nhật Anh:** §5 ≥6 kịch bản + 2 tấn công (phòng chưa chốt, phòng đổi sau khi báo, hai bảng ghi khác nhau, tin giả danh BTC…) · `benchmark.csv` ≥10 câu · `metric_spec.yaml` ≥3 metric · `DATA_CARD.md` (Đức Anh) · canvas dòng 4 (số đầu tiên + 1 trích dẫn) · §1 (Nhật Anh) · hai người chấm độc lập cùng 5 output, ghi `eval/README.md` |
  | **4 · tối T6 → 10:00 T7 (CP3)** | Sáng T7 30 phút: chốt bằng chứng + impact · chạy `run.py eval` lượt 1 cùng nhau, chấm `pass`, `score` · 09:45 đi lại câu chuyện · Cát Tân quay video 30 giây, Nhật Anh nộp CP3 | **Cát Tân + Đức Anh:** nối model thật `ai.py` + code chặn mã phòng không có trong bảng phân công (Cát Tân) · mở rộng 20–30 câu thử: ≥5 `kho`, ≥2 `tu_choi` gồm 2 tấn công, ≥1/3 từ lời người dùng (phỏng vấn, khảo sát câu 9) / data thật (Đức Anh) | **Nhật Anh + Thái Hưng:** `evidence/summary.md`, §0 ảnh chụp email lịch / danh sách nhóm của chính mình (che thông tin), điền số khảo sát vào bảng impact §2 (Nhật Anh) · §3 giải pháp tương tự, `cost/personas.yaml` (số lần hỏi / tháng từ khảo sát), `run.py simulate --try` 10 phiên (Thái Hưng) |
  | **5 · 10:00–13:00 T7** | 30 phút đọc chung các câu trượt → gom nhóm lỗi → chọn 1 cải tiến · *(bonus)* mỗi người cho 1 người ngoài nhóm dùng thử → `validation/log.md` | **Cát Tân + Đức Anh:** cải tiến → `run.py eval` lượt 2 (Cát Tân) · `eval/report.md` + `eval/README.md` (Đức Anh) | **Nhật Anh + Thái Hưng:** `run.py simulate` ≥50 phiên với tỉ lệ đạt lượt 2 · `cost/cost-estimate.md` 3 kịch bản × 2 model, giá có link + ngày xem (Thái Hưng) · cập nhật số §1–§2, bắt đầu slide (Nhật Anh) |
  | **6 · 13:00–14:30 T7 (CP4)** | Go / iterate / stop · tập demo, mỗi người nói một phần: Nhật Anh (pain + impact) · Thái Hưng (giải pháp + chi phí) · Đức Anh (đánh giá) · Cát Tân (demo live) · 14:15 đi lại câu chuyện · Nhật Anh nộp CP4 | **Cát Tân + Đức Anh:** video demo dự phòng · checklist 5.2 (không có key, không có dữ liệu cá nhân) · §9 | **Nhật Anh + Thái Hưng:** slide 8 trang (`slides/outline.md` → PDF) · §8 |
  | **14:30 → 23:59 T7** | Mỗi người một file `reflection/<ten-khong-dau>.md` · sửa theo góp ý | **Nhật Anh:** ghi changelog §10 cho mọi thay đổi sau 14:30 | |
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`): Claude Code đọc đề, đếm hình dạng bộ lịch giả lập `training-ops`, soạn nháp canvas, giả thuyết, spec §0–§2, §10, bộ câu phỏng vấn và khảo sát cho A5. Nhật Anh đọc lại, sửa trước khi commit; số trong bài chỉ lấy từ file có nguồn, không để AI tạo câu trả lời phỏng vấn hay khảo sát.
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
|  |  |  |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
