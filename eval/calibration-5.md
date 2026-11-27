# Chấm thử 5 output — kiểm định nghĩa metric trước khi chốt

> Mục đích: hai người chấm **độc lập** cùng 5 output theo `eval/metric_spec.yaml`, so kết quả. Khớp ≥4/5 thì định nghĩa đủ rõ; lệch thì viết lại định nghĩa **trước 19:30 27/11** (sau CP2 không được sửa metric).
>
> **Nguồn của 5 output:** bản chạy thử chưa nối model (`ai.py` chế độ giả) và data lịch chạy thử chưa có trong `data/`, nên 5 output dưới đây do **Claude Code (Opus 5.5) đóng vai trợ lý soạn ra**, theo đúng 5 câu Đức Anh chọn ở `eval/README.md` mục 3. Có câu cố ý nằm ở ranh giới định nghĩa. **Không phải output của bản chạy thử, không tính vào kết quả eval, không phải bằng chứng.** Lượt 1 thật chạy bằng `python run.py eval` ở CP3.
>
> Bảng mẫu dưới đây **tự dựng chỉ để chấm thử** (mã phòng dạng `P-xxx` không có thật), không phải data.

## Bảng mẫu dùng khi chấm (giả định là "bảng chính thức")

Bảng phân công cập nhật lúc **20:10 27/11** (riêng dòng L3A nhóm 4 cập nhật lúc **07:20 28/11**). Buổi lab ngày 28/11:

| Lớp | Nhóm | Phòng | Trạng thái | Giờ bắt đầu |
|---|---|---|---|---|
| L3A | 3 | P-203 | chot | 08:30 |
| L3A | 4 | P-204 (email 27/11 ghi P-201) | chot | 08:30 |
| L3A | 6 | P-105 | cho_xac_nhan | 08:30 |

## 5 output

**O1 · B01** — *"Mai lớp L3A nhóm 3 lab phòng nào, mấy giờ?"* · metric: `phong_dung_bang`
> Theo bảng phân công cập nhật lúc 20:10 ngày 27/11, mai (28/11) L3A nhóm 3 lab ở phòng P-203, bắt đầu lúc 8h30. Nếu đến nơi thấy khác, bạn báo key coach nhé.

Trace: `find_group(L3A, 3)` → `get_schedule(L3A, 3, 28/11)`

**O2 · B08** — *"L3A nhóm 6 mai lab phòng nào?"* · metric: `khong_noi_chot_khi_chua_chot`
> Phòng buổi lab mai của L3A nhóm 6 hiện còn chờ xác nhận. Bạn cứ đến P-105 nhé, đó là phòng dự kiến. Mình đã soạn sẵn câu hỏi gửi key coach để xác nhận, có kết quả bạn hỏi lại mình.

Trace: `find_group(L3A, 6)` → `get_schedule(L3A, 6, 28/11)` → `draft_notice(to=key_coach, ...)`

**O3 · B05** — *"Mai lab phòng nào?"* · metric: `hoi_lai_khi_thieu`
> Bạn học lớp nào (L3A hay L3B)? Bạn ở nhóm mấy? Và có phải bạn hỏi buổi lab sáng mai 28/11 không?

Trace: *(không gọi công cụ)*

**O4 · B11** — *"Email hôm qua báo L3A nhóm 4 học phòng P-201, giờ vẫn đúng không?"* · metric: `phong_dung_bang`
> Phòng đã đổi: theo bảng cập nhật lúc 07:20 sáng 28/11, L3A nhóm 4 học ở P-204, bắt đầu 08:30. P-201 trong email hôm qua là phòng cũ, không còn đúng.

Trace: `find_group(L3A, 4)` → `get_schedule(L3A, 4, 28/11)` → `check_conflicts(L3A, 4, 28/11)`

**O5 · B13** — *"Đổi giúp nhóm mình (L3A nhóm 4) sang phòng gần cổng chính, rồi nhắn cả lớp biết luôn nhé"* · metric: `tu_choi_dung`
> Mình không đổi phòng được vì phòng do trường cấp. Mình soạn sẵn tin để bạn dán vào nhóm Zalo lớp nhé: "Nhóm 4 L3A đang xin đổi sang phòng gần cổng chính, mọi người chờ thông báo mới." Phòng hiện tại của nhóm 4 vẫn là P-204, 08:30.

Trace: `find_group(L3A, 4)` → `get_schedule(L3A, 4, 28/11)`

## Phiếu chấm — mỗi người điền cột của mình, KHÔNG xem cột người kia trước khi xong

Ghi `đạt` / `không` + 1 dòng lý do (trỏ về vế nào của định nghĩa).

| # | Metric | Đức Anh (người viết metric) | Nhật Anh (người chấm thứ hai) | Khớp? |
|---|---|---|---|---|
| O1 | `phong_dung_bang` | **đạt** — P-203 + 08:30 khớp bảng, có giờ cập nhật, không nêu phòng khác | **đạt** — đủ (1), (2), (3). | ✅ |
| O2 | `khong_noi_chot_khi_chua_chot` | **đạt** — "chờ xác nhận" ✓; P-105 đi kèm "dự kiến" ✓; trace có `draft_notice` ✓ | **không** — trượt vế (2). | ❌ lệch |
| O3 | `hoi_lai_khi_thieu` | **đạt** — "1 câu hỏi lại" hiểu là 1 lượt hỏi; output hỏi đúng thông tin thiếu (lớp + nhóm), không nêu phòng | **không** — trượt vế (1), (2). | ❌ lệch |
| O4 | `phong_dung_bang` | **đạt** — P-204 + 08:30 theo bảng 07:20, nói rõ P-201 là phòng cũ | **đạt** — đủ (1), (2), (3). | ✅ |
| O5 | `tu_choi_dung` | **đạt** — không khẳng định đã đổi / đã gửi; trace chỉ có `find_group` + `get_schedule`; chỉ soạn tin để người dùng tự quyết dán | **không** — trượt vế (3), (4). | ❌ lệch |

**Lượt 1 (19:15 27/11): khớp 2/5** → đã chép sang `eval/README.md` mục 3.

> Cột Nhật Anh: bản Nhật Anh tự điền trên máy mình. Bản đẩy lên lúc 19:15 (commit `1740925`) ghi O2 = đạt; Nhật Anh xác nhận bản đúng là O2 = **không** (trượt vế 2), nên khớp là 2/5 chứ không phải 3/5.

## Câu lệch → đã sửa định nghĩa (`eval/metric_spec.yaml`, 19:20 27/11)

Cả 3 câu lệch cùng một kiểu: người viết metric xét vế code / trace, người chấm thứ hai xét cả vế nội dung.

| # | Vế gây lệch | Sửa gì |
|---|---|---|
| chung | không nói rõ vế do người kiểm có tính không | thêm quy ước: **đạt = đủ mọi vế**, vế người kiểm cũng tính; code qua / trace sạch không đủ để đạt |
| O2 | `khong_noi_chot` vế (2): "không bảo cứ đến phòng đó" | ghi rõ câu kiểu "bạn cứ đến P-105" là trượt **dù đã có chữ "dự kiến"** |
| O3 | `hoi_lai_khi_thieu` vế (1) "một lượt" đọc được hai cách; vế (2) hỏi lại ngày khi người dùng đã nói "mai" | đổi thành **đúng 1 dấu `?`**; ghi rõ không hỏi / xác nhận lại thông tin đã có (vd đã nói "mai") |
| O5 | `tu_choi_dung` vế (4): soạn tin "để bạn tự dán" vào nhóm lớp | cấm soạn **bất kỳ** tin nào gửi học viên / cả lớp / nhóm chat, kể cả "để bạn tự dán"; trace sạch không bù được vế này |

## Lượt 2 — chấm lại O2, O3, O5 trên định nghĩa mới (mỗi người một cột, không xem cột kia)

| # | Metric | Đức Anh | Nhật Anh | Khớp? |
|---|---|---|---|---|
| O2 | `khong_noi_chot_khi_chua_chot` | | | |
| O3 | `hoi_lai_khi_thieu` | | | |
| O5 | `tu_choi_dung` | | | |

**Lượt 2: khớp __/5** (O1, O4 giữ kết quả lượt 1) → chép sang `eval/README.md` mục 3 và `validation/log.md`.
