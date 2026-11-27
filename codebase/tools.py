"""Công cụ của bài toán — trợ lý phòng lab (spec.md §4). Đọc data chạy thử trong data/ (xem data/DATA_CARD.md).

Mỗi công cụ là một hàm có @tool; docstring ghi: tên · input · output · có tác động ra ngoài không.
Không công cụ nào gửi tin hay sửa dữ liệu. draft_notice chỉ tạo bản nháp chờ key coach duyệt.
"""
import csv
import os
import unicodedata

from tracing import tool, TOOLS  # noqa: F401  (TOOLS: danh sách công cụ đã đăng ký)

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def _load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return list(csv.DictReader(f))


OFFICIAL = _load("lich_chinh_thuc.csv")
LAB_COACH = [r for r in _load("lich_lab_coach.csv") if r["nguon"] == "lich_lab_2604_0805"]  # bảng lab coach hiện hành
HISTORY = _load("lich_su_sua.csv")
GROUPS = _load("nhom.csv")


def _rooms(s):
    return [x for x in s.split(";") if x]


def _fold(s):
    """Bỏ dấu, chữ thường, gộp khoảng trắng — để so tên gõ không dấu."""
    s = unicodedata.normalize("NFD", s.replace("đ", "d").replace("Đ", "D"))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return " ".join(s.lower().split())


def room_of_group(rooms, nhom):
    """Quy tắc tự dựng (data/DATA_CARD.md, Dataset 1b): nhóm g ngồi phòng thứ ((g-1) mod k)+1 trong danh sách."""
    return rooms[(int(nhom) - 1) % len(rooms)] if rooms and nhom else ""


@tool
def get_schedule(date: str, lop: str, nhom: int = 0, buoi_lab: str = "") -> list:
    """get_schedule · input: date (YYYY-MM-DD, có thể rỗng nếu có buoi_lab), lop (L3A / L3B),
    nhom (số nhóm, 0 = chưa biết), buoi_lab (vd "LAB 10", tuỳ chọn) · output: danh sách buổi LAB khớp trong
    bảng phân công chính thức mới nhất: ngày, ca, buổi, giờ, trạng thái, phòng của nhóm (nếu biết nhóm),
    danh sách phòng, giờ cập nhật bảng · KHÔNG tác động ra ngoài (chỉ đọc)."""
    out = []
    for r in OFFICIAL:
        if r["lop"] != lop:
            continue
        if date and r["ngay"] != date:
            continue
        if buoi_lab and r["buoi_lab"].replace(" ", "").upper() != buoi_lab.replace(" ", "").upper():
            continue
        if not date and not buoi_lab:
            continue
        rooms, dk = _rooms(r["phong"]), _rooms(r["phong_du_kien"])
        out.append({
            "ngay": r["ngay"], "ca": r["ca"], "lop": r["lop"], "buoi_lab": r["buoi_lab"],
            "gio_bat_dau": r["gio_bat_dau"], "gio_ket_thuc": r["gio_ket_thuc"], "trang_thai": r["trang_thai"],
            "phong_cac_nhom": rooms, "phong_du_kien_cac_nhom": dk,
            "phong_nhom": room_of_group(rooms, nhom), "phong_du_kien_nhom": room_of_group(dk, nhom),
            "bang_cap_nhat": r["bang_cap_nhat"], "o_sua_lan_cuoi": r["o_sua_lan_cuoi"], "o": r["o"],
        })
    return out


@tool
def find_group(lop: str, query: str) -> list:
    """find_group · input: lop (L3A / L3B), query (số nhóm, hoặc họ tên học viên như người dùng gõ) ·
    output: danh sách nhóm khớp [{"lop", "nhom"}]; tên so sau khi bỏ dấu và chữ hoa, phải khớp đủ cả tên,
    không đoán tên gần giống → 0 hoặc >1 kết quả thì agent hỏi lại · KHÔNG tác động ra ngoài (chỉ đọc).
    Không trả tên người khác ra ngoài."""
    q = str(query).strip()
    if q.isdigit():
        found = {int(g["nhom"]) for g in GROUPS if g["lop"] == lop and int(g["nhom"]) == int(q)}
    else:
        fq = _fold(q)
        found = {int(g["nhom"]) for g in GROUPS if g["lop"] == lop and _fold(g["thanh_vien"]) == fq}
    return [{"lop": lop, "nhom": n} for n in sorted(found)]


@tool
def check_conflicts(session: dict) -> dict:
    """check_conflicts · input: một buổi từ get_schedule · output: {"tinh_trang": "chot" | "cho_xac_nhan" |
    "lech", "chi_tiet": str, "lan_doi": [...]} — so bảng chính thức với bảng lab coach cùng buổi (code, không AI),
    kèm các lần đổi phòng sau khi đã chốt (lịch sử chỉnh sửa) · KHÔNG tác động ra ngoài (chỉ đọc)."""
    lc = next((r for r in LAB_COACH if r["ngay"] == session["ngay"] and r["lop"] == session["lop"]
               and r["buoi_lab"] == session["buoi_lab"]), None)
    lan_doi = [h for h in HISTORY if h["o"] == session["o"] and h["truoc"].startswith("Phòng: ")
               and "chờ xác nhận" not in h["truoc"]]
    status, detail = session["trang_thai"], ""
    if lc:
        # Lệch = trạng thái khác nhau (vd một bảng chốt, bảng kia chờ xác nhận), hoặc cả hai đều ghi phòng mà khác nhau.
        # Hai bảng cùng "chờ xác nhận", chỉ một bảng có phòng dự kiến: không tính lệch (cùng là chưa chốt).
        off = session["phong_cac_nhom"] or session["phong_du_kien_cac_nhom"]
        other = _rooms(lc["phong"] or lc["phong_du_kien"])
        if lc["trang_thai"] != session["trang_thai"] or (off and other and off != other):
            status = "lech"
            detail = "bảng chính thức: %s %s · bảng lab coach: %s %s" % (
                session["trang_thai"], ";".join(session["phong_cac_nhom"] or session["phong_du_kien_cac_nhom"]),
                lc["trang_thai"], lc["phong"] or lc["phong_du_kien"])
    return {"tinh_trang": status, "chi_tiet": detail,
            "lan_doi": [{"thoi_diem": h["thoi_diem"], "truoc": h["truoc"], "sau": h["sau"]} for h in lan_doi]}


@tool
def draft_notice(lop: str, changes: list) -> dict:
    """draft_notice · input: lop, changes (danh sách {buoi, nhom, van_de}) · output: BẢN NHÁP câu hỏi cho key coach,
    trang_thai "cho_duyet" · KHÔNG gửi: không có hàm gửi nào; key coach đọc, duyệt rồi tự gửi qua kênh chính thức."""
    lines = ["- %s, nhóm %s: %s" % (c.get("buoi", ""), c.get("nhom", "?"), c.get("van_de", "")) for c in changes]
    return {"gui_toi": "key coach %s" % lop, "trang_thai": "cho_duyet",
            "noi_dung": "Học viên %s hỏi phòng buổi lab, bảng phân công chưa đủ căn cứ để trả lời:\n%s\n"
                        "Nhờ key coach xác nhận phòng chính thức." % (lop, "\n".join(lines))}
