"""Tách data chạy thử từ bộ giả lập training-ops của BTC -> các file csv nhỏ trong data/.

Chạy:  python data/build_data.py
Đọc:   data-btc/training-ops/teaching-schedule.xlsx, lab-coach-schedule.xlsx  (nguyên file BTC, KHÔNG commit)
Ghi:   data/lich_chinh_thuc.csv   buổi LAB của L3A / L3B trong bảng phân công chính thức (sheet "Khoá 9 (GĐ1)")
       data/lich_lab_coach.csv    phòng của cùng các buổi đó trong file lab coach (2 nguồn: sheet lịch lab đợt 2, bản chép lịch 12/04)
       data/lich_su_sua.csv       các lần sửa ô LAB của L3 (sheet "Lịch sử chỉnh sửa"), bỏ cột người sửa
       data/nhom.csv              danh sách nhóm TỰ DỰNG (synthetic): data BTC không có bảng nhóm -> phòng

Chỉ dùng thư viện chuẩn (đọc xlsx bằng zipfile + xml). Bỏ tên giảng viên / lab coach, email, link: trợ lý không cần.
"""
import csv
import os
import re
import zipfile
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data-btc", "training-ops")
OUT = os.path.join(ROOT, "data")

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
CA = {"Sáng": ("sang", "09:00", "13:00"), "Chiều": ("chieu", "14:00", "18:00")}
ROOM = re.compile(r"\b[A-H]\d{3}\b")


# ---------- đọc xlsx bằng thư viện chuẩn ----------
def _col(ref):
    n = 0
    for ch in re.match(r"[A-Z]+", ref).group(0):
        n = n * 26 + ord(ch) - 64
    return n  # A = 1


def read_xlsx(path):
    """-> {tên sheet: {(dòng, cột): giá trị}} (cột tính từ 1; ô gộp chỉ có giá trị ở ô đầu)."""
    z = zipfile.ZipFile(path)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS):
            shared.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = {r.get("Id"): r.get("Target") for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
    sheets = {}
    for s in wb.find("m:sheets", NS):
        target = rels[s.get("{%s}id" % NS["r"])].lstrip("/")
        target = target if target.startswith("xl/") else "xl/" + target
        cells = {}
        for c in ET.fromstring(z.read(target)).iter("{%s}c" % NS["m"]):
            v = c.find("m:v", NS)
            t = c.get("t")
            if t == "s" and v is not None:
                val = shared[int(v.text)]
            elif t == "inlineStr":
                val = "".join(x.text or "" for x in c.iter("{%s}t" % NS["m"]))
            else:
                val = v.text if v is not None else ""
            ref = c.get("r")
            cells[(int(re.search(r"\d+", ref).group(0)), _col(ref))] = val
        sheets[s.get("name")] = cells
    return sheets


def rooms(text):
    return ";".join(ROOM.findall(text))


def iso(d):  # 27/04/2027 -> 2027-04-27
    dd, mm, yy = d.split("/")
    return "%s-%s-%s" % (yy, mm, dd)


def history_time(s):  # "26/04/2027 22:30" -> "2027-04-26 22:30"
    d, t = s.split(" ")
    return iso(d) + " " + t


# ---------- 1. bảng phân công chính thức ----------
def parse_cell(text):
    """Ô lịch nhiều dòng -> dict. None nếu ô không phải buổi LAB của L3A / L3B."""
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    if not lines:
        return None
    m = re.match(r"(L3A|L3B)\s+—\s+LAB\s+(\d+)", lines[0])
    if not m:
        return None
    r = {"lop": m.group(1), "buoi_lab": "LAB " + m.group(2), "gio_rieng": "", "online": False,
         "trang_thai": "", "phong": "", "phong_du_kien": "", "chu_de": ""}
    for l in lines[1:]:
        if l == "Online":
            r["online"] = True
        elif re.fullmatch(r"\d{1,2}:\d{2}\s*[–-]\s*\d{1,2}:\d{2}", l):
            r["gio_rieng"] = l
        elif l.startswith("Phòng dự kiến:"):
            r["trang_thai"], r["phong_du_kien"] = "cho_xac_nhan", rooms(l)
        elif l.startswith("Phòng: chờ xác nhận"):
            r["trang_thai"] = "cho_xac_nhan"
        elif l.startswith("Phòng:"):
            r["trang_thai"], r["phong"] = "chot", rooms(l)
        elif l.startswith("Giảng Viên") or l.startswith("Phòng thêm"):
            continue
        elif not r["chu_de"]:
            r["chu_de"] = l
    if r["online"]:
        r["trang_thai"] = "online"
    return r


def build_official(ts, history):
    sh = ts["Khoá 9 (GĐ1)"]
    export = sh.get((1, 4), "")  # "Bản xuất 27/04/2027 21:00"
    m = re.search(r"(\d{2}/\d{2}/\d{4}) (\d{2}:\d{2})", export)
    bang_cap_nhat = history_time(m.group(1) + " " + m.group(2))
    last_edit = {}
    for h in history:
        last_edit[h["o"]] = max(last_edit.get(h["o"], ""), h["thoi_diem"])
    out, ngay = [], ""
    max_row = max(r for r, _ in sh)
    for row in range(6, max_row + 1):
        if sh.get((row, 1)):
            ngay = iso(sh[(row, 1)])
        ca_raw = sh.get((row, 3), "")
        ca = next((v for k, v in CA.items() if ca_raw.startswith(k)), None)
        if not ca:
            continue
        r = parse_cell(sh.get((row, 6), ""))  # cột F = LAB của L3
        if not r:
            continue
        bd, kt = ca[1], ca[2]
        if r["gio_rieng"]:
            bd, kt = [x.strip() for x in re.split(r"[–-]", r["gio_rieng"])]
        o = "F%d" % row
        out.append({"ngay": ngay, "ca": ca[0], "lop": r["lop"], "buoi_lab": r["buoi_lab"],
                    "gio_bat_dau": bd, "gio_ket_thuc": kt, "trang_thai": r["trang_thai"],
                    "phong": r["phong"], "phong_du_kien": r["phong_du_kien"], "chu_de": r["chu_de"],
                    "o_sua_lan_cuoi": last_edit.get(o, ""), "bang_cap_nhat": bang_cap_nhat, "o": o})
    return out


def build_history(ts):
    sh = ts["Lịch sử chỉnh sửa"]
    out = []
    for row in range(2, max(r for r, _ in sh) + 1):
        o, buoi = sh.get((row, 4), ""), sh.get((row, 5), "")
        if not o.startswith("F") or not re.search(r"L3[AB] — LAB", buoi):
            continue
        out.append({"thoi_diem": history_time(sh[(row, 1)]), "o": o, "buoi": buoi,
                    "truoc": sh.get((row, 6), ""), "sau": sh.get((row, 7), "")})
    return out


# ---------- 2. file lab coach ----------
def lc_status(raw):
    raw = raw.strip()
    if raw.startswith("dk:"):
        return "cho_xac_nhan", "", rooms(raw)
    if "chờ xác nhận" in raw:
        return "cho_xac_nhan", "", rooms(raw)
    return ("chot", rooms(raw), "") if rooms(raw) else ("", "", "")


def build_lab_coach(lc):
    out, seen = [], set()
    sh = lc["Lịch lab 2604-0805"]  # cột K–P: Ngày, Lớp, Session, Phòng, Buổi, Key Coach
    for row in sorted({r for r, _ in sh}):
        ngay, lop, ses, phong, buoi = (sh.get((row, c), "") for c in (11, 12, 13, 14, 15))
        if lop not in ("L3A", "L3B") or not ses.startswith("LAB") or not re.match(r"\d{2}/\d{2}/\d{4}", ngay):
            continue
        key = (ngay, lop, ses)
        if key in seen:
            continue
        seen.add(key)
        st, p, dk = lc_status(phong)
        out.append({"nguon": "lich_lab_2604_0805", "ngay": iso(ngay), "ca": CA.get(buoi, ("",))[0],
                    "lop": lop, "buoi_lab": ses, "trang_thai": st, "phong": p, "phong_du_kien": dk})
    sh = lc["Lịch lớp K9 (bản chép)"]  # cùng dạng bảng chính thức, chép ngày 12/04
    ngay = ""
    for row in range(6, max(r for r, _ in sh) + 1):
        if sh.get((row, 1)):
            ngay = iso(sh[(row, 1)])
        r = parse_cell(sh.get((row, 6), ""))
        ca = next((v for k, v in CA.items() if sh.get((row, 3), "").startswith(k)), None)
        if not r or not ca:
            continue
        out.append({"nguon": "ban_chep_1204", "ngay": ngay, "ca": ca[0], "lop": r["lop"],
                    "buoi_lab": r["buoi_lab"], "trang_thai": r["trang_thai"],
                    "phong": r["phong"], "phong_du_kien": r["phong_du_kien"]})
    return out


# ---------- 3. danh sách nhóm tự dựng ----------
HO = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Vũ", "Đặng", "Bùi", "Đỗ", "Ngô", "Dương", "Lý"]
DEM = ["Văn", "Thị", "Minh", "Thu", "Quốc", "Ngọc", "Gia", "Thanh"]
TEN = ["An", "Bình", "Châu", "Dũng", "Giang", "Hà", "Hiếu", "Khoa", "Lan", "Long", "Mai", "Nam",
       "Nga", "Phúc", "Quân", "Sơn", "Tâm", "Thảo", "Trang", "Tuấn", "Uyên", "Việt", "Xuân", "Yến"]
SO_NHOM, SO_TV = 12, 4  # (tự ước tính) ~350 HV / lớp, chỉ dựng 4 tên mẫu / nhóm cho câu thử tra theo tên


def build_groups():
    """Tên mẫu ghép từ 3 danh sách, không trùng nhau (bước 37 nguyên tố cùng nhau với 12*8*24 tổ hợp)."""
    combos = [(h, d, t) for h in HO for d in DEM for t in TEN]
    out, i = [], 0
    for lop in ("L3A", "L3B"):
        for nhom in range(1, SO_NHOM + 1):
            for _ in range(SO_TV):
                out.append({"lop": lop, "nhom": nhom, "thanh_vien": " ".join(combos[(i * 37) % len(combos)])})
                i += 1
    assert len({r["thanh_vien"] for r in out}) == len(out), "tên mẫu bị trùng"
    return out


def write(name, rows):
    path = os.path.join(OUT, name)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("  %-22s %4d dòng" % (name, len(rows)))


def main():
    ts = read_xlsx(os.path.join(SRC, "teaching-schedule.xlsx"))
    lc = read_xlsx(os.path.join(SRC, "lab-coach-schedule.xlsx"))
    hist = build_history(ts)
    official = build_official(ts, hist)
    print("Ghi vào data/:")
    write("lich_chinh_thuc.csv", official)
    write("lich_lab_coach.csv", build_lab_coach(lc))
    write("lich_su_sua.csv", hist)
    write("nhom.csv", build_groups())
    by = {}
    for r in official:
        by[r["trang_thai"]] = by.get(r["trang_thai"], 0) + 1
    print("  trạng thái buổi LAB chính thức:", by)


if __name__ == "__main__":
    main()
