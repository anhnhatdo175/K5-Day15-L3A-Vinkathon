"""Đếm số liệu bằng chứng từ data/preclass/ (BTC cấp), chỉ dùng thư viện chuẩn của Python.

Chạy:   python evidence/count_preclass.py [đường-dẫn-tới-thư-mục-preclass]
Mặc định đọc data-btc/preclass/, chép thư mục data/preclass/ của repo đề vào đó.
data-btc/ đã có trong .gitignore: KHÔNG commit nguyên file data.

Định nghĩa từng số (đếm gì · trên tập nào · mẫu số): evidence/data-mining.md mục 1.
Chạy lại phải ra đúng các số trong evidence/data-mining.md mục 3.
"""
import csv
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "data-btc", "preclass")
NIGHT = {22, 23, 0, 1}  # 22:00–01:59 giờ Việt Nam


def rows(name):
    with open(os.path.join(D, name), encoding="utf-8-sig", newline="") as f:
        yield from csv.DictReader(f)


def vn_time(s):
    """Mốc giờ trong data là UTC (README data: 'Giờ là UTC'); giờ Việt Nam = UTC + 7."""
    if not (s.endswith("+00:00") or s.endswith("Z")):
        raise ValueError("mốc giờ không phải UTC: " + s)
    return datetime.strptime(s[:19], "%Y-%m-%dT%H:%M:%S") + timedelta(hours=7)


def payload(r):
    s = r.get("data") or ""
    return json.loads(s) if s.startswith("{") else {}


def pct(x, n):
    return "%d/%d (%.0f%%)" % (x, n, 100.0 * x / n) if n else "%d/0" % x


if not os.path.exists(os.path.join(D, "events.csv")):
    sys.exit("Không thấy %s/events.csv, chép data/preclass/ của repo đề vào data-btc/preclass/ "
             "hoặc truyền đường dẫn: python evidence/count_preclass.py <thư-mục-preclass>" % D)

# ---------- chat.csv: một dòng = một lượt học viên nhắn AI ----------
chat = {r["id"]: r for r in rows("chat.csv")}
ta_ids = {cid for cid, r in chat.items() if r["addressed_agent_id"] == "teaching_assistant"}

# ---------- events.csv: một lượt đọc ----------
active = set()                      # học viên có >=1 sự kiện actor = learner
lesson_days = defaultdict(set)      # hv -> các ngày học (dayNN trong lesson_id) đã chạm
video_hv, night_hv = set(), set()   # hv có mở video / có mở video lúc 22h–02h
opened, ended = set(), set()        # cặp (hv, video)
rewind_hv = set()
rewinds = defaultdict(int)          # (hv, video) -> số lần tua lui
opens = defaultdict(int)            # (hv, video) -> số lần mở
link_seeks = []                     # (hv, giờ VN) các lần tua có by = link
ta_replies = []                     # (chat id, payload, giờ VN) trả lời của trợ giảng
reply_times = defaultdict(list)     # hv -> giờ VN các lần trợ giảng trả lời
shown = set()                       # cặp (hv, intervention_id) bạn học AI xen vào
shown_hv = set()
lab_done = lab_skipped = 0
open_events = night_open_events = 0
so_hieu_hv = set()                  # hv có mở Sổ hiểu bài

for r in rows("events.csv"):
    typ, hv, actor = r["type"], r["hv"], r["actor"]
    if actor == "learner":
        active.add(hv)
        m = re.search(r"day(\d\d)", r["lesson_id"] or "")
        if m:
            lesson_days[hv].add(m.group(1))
    if typ == "video_opened" and actor == "learner":
        video_hv.add(hv)
        open_events += 1
        if vn_time(r["occurred_at"]).hour in NIGHT:
            night_hv.add(hv)
            night_open_events += 1
        if r["video"]:
            opened.add((hv, r["video"]))
            opens[(hv, r["video"])] += 1
    elif typ == "video_ended" and actor == "learner":
        ended.add((hv, r["video"]))
    elif typ == "video_seeked" and actor == "learner":
        d = payload(r)
        if (d.get("to") or 0) - (d.get("from") or 0) < 0:
            rewind_hv.add(hv)
            rewinds[(hv, r["video"])] += 1
        if d.get("by") == "link":
            link_seeks.append((hv, vn_time(r["occurred_at"])))
    elif typ == "agent_replied" and r["ref_id"] in ta_ids:
        t = vn_time(r["occurred_at"])
        ta_replies.append((r["ref_id"], payload(r), t))
        reply_times[hv].append(t)
    elif typ == "agent_message_shown":
        iid = payload(r).get("intervention_id")
        if iid:
            shown.add((hv, iid))
            shown_hv.add(hv)
    elif typ == "lab_completed" and actor == "learner":
        lab_done += 1
        lab_skipped += payload(r).get("skipped") is True
    elif typ == "so_hieu_bai_opened" and actor == "learner":
        so_hieu_hv.add(hv)

# ---------- tính số ----------
ta_hv = {chat[c]["hv"] for c in ta_ids}
with_key = [x for x in ta_replies if "moc_trich_dan" in x[1]]
cited = [x for x in with_key if x[1]["moc_trich_dan"]]
mc_known = [x for x in ta_replies if "missing_context" in x[1]]
mc_true = [x for x in mc_known if x[1]["missing_context"] is True]
short_q = sorted(c for c in ta_ids if int(float(chat[c]["do_dai_cau_hoi"] or 0)) <= 10)
replied_pairs = {(r["hv"], r["intervention_id"]) for r in chat.values() if r["intervention_id"]}
day1 = [hv for hv, s in lesson_days.items() if "01" in s]


def link_after_reply(hv, t, minutes=10):
    return any(timedelta(0) <= t - tr <= timedelta(minutes=minutes) for tr in reply_times.get(hv, []))


link_hv = {hv for hv, _ in link_seeks}
link_near = [x for x in link_seeks if link_after_reply(*x)]

print("Data:", D)
print("\n== Hướng A1 · trợ giảng dưới video ==")
print("M1 cặp (học viên, video) đã mở mà xem tới cuối (video_ended):", pct(len(opened & ended), len(opened)))
by_day = defaultdict(lambda: [0, 0])  # ngày học của video (dNN trong mã video) -> [xem tới cuối, đã mở]
for p in opened:
    m = re.match(r"d(\d\d)-", p[1])
    if m:
        by_day[m.group(1)][0] += p in ended
        by_day[m.group(1)][1] += 1
print("   theo ngày học của video:", " · ".join("D%s %s" % (k, pct(*v)) for k, v in sorted(by_day.items())))
print("M2 học viên có >=1 lần tua lui (to < from) / học viên có mở video:", pct(len(rewind_hv), len(video_hv)))
print("M3 học viên có >=1 lần mở video lúc 22h–02h giờ VN / học viên có mở video:", pct(len(night_hv), len(video_hv)),
      "· lượt mở video lúc 22h–02h:", pct(night_open_events, open_events))
print("M4 học viên từng nhắn trợ giảng AI / học viên có hoạt động:", pct(len(ta_hv), len(active)))
print("M5 câu trả lời của trợ giảng có >=1 mốc trích dẫn / câu có ghi khoá moc_trich_dan:", pct(len(cited), len(with_key)),
      "· khoá này có từ", min(t for _, _, t in with_key).strftime("%d/%m/%Y"))
print("M6 lần tua bằng 'link' (by = link):", len(link_seeks), "lần ·", len(link_hv), "học viên ·",
      len(link_near), "lần xảy ra trong 10 phút sau một câu trả lời của trợ giảng")
print("M7 câu trả lời của trợ giảng có missing_context = true / câu có ghi khoá:", pct(len(mc_true), len(mc_known)))
print("M8 câu hỏi gửi trợ giảng dài <= 10 ký tự / câu hỏi gửi trợ giảng:", pct(len(short_q), len(ta_ids)))

print("\n== Số cho các hướng so sánh (spec.md §2) ==")
print("M9 học viên học Day01 có chạm Day08:", pct(sum("08" in lesson_days[h] for h in day1), len(day1)))
print("M10 cặp (học viên, lượt bạn học AI xen vào) được học viên đó trả lời:", pct(len(shown & replied_pairs), len(shown)),
      "·", len(shown_hv), "học viên thấy lời xen vào,", len({h for h, _ in replied_pairs}), "học viên từng trả lời")
print("M11 lần xong mini lab là bấm 'bỏ qua' (lab_completed skipped = true):", pct(lab_skipped, lab_done))
print("   (bối cảnh) học viên có mở Sổ hiểu bài:", len(so_hieu_hv))

print("\n== Ví dụ cụ thể (mã đã ẩn danh, không đoán ai là ai) ==")
ex = sorted(p for p in opened if p not in ended and rewinds.get(p, 0) >= 5)
if ex:
    p = ex[0]
    print("V1 học viên %s · video %s: mở %d lần, tua lui %d lần, không có video_ended" % (p[0], p[1], opens[p], rewinds[p]))
if short_q:
    c = chat[short_q[0]]
    print("V2 lượt chat %s: câu hỏi gửi trợ giảng dài %s ký tự, trợ giảng trả lời %s ký tự (video %s)"
          % (short_q[0], c["do_dai_cau_hoi"], c["do_dai_tra_loi"], c["transcript"]))
nocite = sorted(c for c, d, _ in with_key if not d["moc_trich_dan"])
if nocite:
    c = chat[nocite[0]]
    print("V3 lượt chat %s: trợ giảng trả lời %s ký tự, không kèm mốc trích dẫn nào (moc_trich_dan = [])"
          % (nocite[0], c["do_dai_tra_loi"]))
mcs = sorted(c for c, _, _ in mc_true)
if mcs:
    c = chat[mcs[0]]
    print("V4 lượt chat %s: câu trả lời có missing_context = true, dài %s ký tự (câu hỏi %s ký tự)"
          % (mcs[0], c["do_dai_tra_loi"], c["do_dai_cau_hoi"]))
if link_near:
    hv, t = sorted(link_near)[0]
    print("V5 học viên %s: tua bằng 'link' lúc %s, trong 10 phút sau một câu trả lời của trợ giảng" % (hv, t.strftime("%d/%m %H:%M")))
