"""Giao diện web của bản chạy thử — phần dùng chung cho máy mình (codebase/app.py) và Vercel (api/answer.py).

    GET  /             trang chat (public/index.html)
    GET  /api/answer   thông tin bản chạy thử: model đang dùng, mốc "hôm nay"
    POST /api/answer   {"text": "..."} → answer(text) trong agent.py, kèm tóm tắt trace của lượt hỏi

Mỗi lượt hỏi vẫn đi qua tracing.begin / end như codebase/app.py bản dòng lệnh. Giao diện chỉ HIỂN THỊ bản nháp
draft_notice tạo ra (chờ key coach duyệt), không gửi đi đâu. Chỉ dùng thư viện chuẩn.
"""
import json
import os
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
INDEX = os.path.join(ROOT, "public", "index.html")
MAX_CHARS = 1000  # câu hỏi dài hơn thì từ chối, không gọi model

sys.path.insert(0, HERE)
import agent  # noqa: E402
import ai  # noqa: E402
import tools  # noqa: E402
import tracing  # noqa: E402

# tracing giữ trạng thái chung cho một lượt hỏi → mỗi lúc chỉ chạy một lượt.
_LOCK = threading.Lock()
_drafts = []
_draft_notice = agent.draft_notice


def _draft_and_keep(*args, **kwargs):
    """Gọi đúng công cụ draft_notice (vẫn ghi trace), giữ lại bản nháp để giao diện hiển thị."""
    res = _draft_notice(*args, **kwargs)
    _drafts.append(res)
    return res


agent.draft_notice = _draft_and_keep

# Giữ kết quả ĐẦY ĐỦ của get_schedule / check_conflicts (trace chỉ giữ bản rút gọn) để cột "Căn cứ" hiển thị.
# Vẫn gọi đúng công cụ đã đăng ký @tool nên trace không đổi.
_sessions = []
_get_schedule = agent.get_schedule
_check_conflicts = agent.check_conflicts


def _schedule_and_keep(*args, **kwargs):
    res = _get_schedule(*args, **kwargs)
    for s in res:
        if not any(x["o"] == s["o"] for x in _sessions):
            _sessions.append(dict(s))
    return res


def _conflicts_and_keep(session, *args, **kwargs):
    res = _check_conflicts(session, *args, **kwargs)
    for s in _sessions:
        if s["o"] == session.get("o"):
            s["kiem_tra"] = res
    return res


agent.get_schedule = _schedule_and_keep
agent.check_conflicts = _conflicts_and_keep


def _upcoming(limit=10):
    """Các buổi LAB của L3 từ "hôm nay" trở đi trong bảng chính thức — cột trái hiển thị làm bối cảnh."""
    today = agent.HOM_NAY.isoformat()
    rows = sorted((r for r in tools.OFFICIAL if r["ngay"] >= today), key=lambda r: (r["ngay"], r["gio_bat_dau"]))
    return [{"ngay": r["ngay"], "thu": agent.fmt_day(r["ngay"]), "ca": r["ca"], "lop": r["lop"],
             "buoi_lab": r["buoi_lab"], "gio": r["gio_bat_dau"], "trang_thai": r["trang_thai"]} for r in rows[:limit]]


def info():
    days = [agent.HOM_NAY + agent.dt.timedelta(days=i) for i in range(1, 6)]
    return {"model": ai.MODEL_NAME if ai.MODEL_PROVIDER != "fake" else "fake",
            "provider": ai.MODEL_PROVIDER,
            "hom_nay": "%s %s" % (agent.THU[agent.HOM_NAY.weekday()], agent.HOM_NAY.strftime("%d/%m/%Y")),
            "hom_nay_iso": agent.HOM_NAY.isoformat(),
            "ngay_toi": [{"iso": d.isoformat(), "nhan": agent.fmt_day(d.isoformat()), "mai": i == 0}
                         for i, d in enumerate(days)],
            "so_nhom": max(int(g["nhom"]) for g in tools.GROUPS),
            "lich_toi": _upcoming(),
            "bang_cap_nhat": agent.fmt_update(tools.OFFICIAL[0]["bang_cap_nhat"]) if tools.OFFICIAL else "",
            "max_chars": MAX_CHARS}


def _steps(events):
    out = []
    for e in events:
        if e["kind"] == "note":
            out.append({"kind": "note", "text": e["text"]})
        elif e["kind"] == "tool":
            out.append({"kind": "tool", "name": e["name"], "input": e.get("input", ""),
                        "output": e.get("output", ""), "latency_s": e.get("latency_s"), "error": e.get("error")})
        elif e["kind"] == "model":
            out.append({"kind": "model", "name": e["name"], "model": e.get("model", ""),
                        "tokens_in": e.get("tokens_in", 0), "tokens_out": e.get("tokens_out", 0),
                        "output": e.get("output", ""), "latency_s": e.get("latency_s"), "error": e.get("error")})
    return out


def ask(text):
    """Một lượt hỏi. Trả (mã HTTP, dict)."""
    text = (text or "").strip()
    if not text:
        return 400, {"error": "Câu hỏi đang trống."}
    if len(text) > MAX_CHARS:
        return 400, {"error": "Câu hỏi dài quá %d ký tự." % MAX_CHARS}
    with _LOCK:
        del _drafts[:]
        del _sessions[:]
        tracing.begin("web")
        t0 = time.perf_counter()
        try:
            result = agent.answer(text)
            failure = None
        except NotImplementedError as e:
            result, failure = None, (500, "Chưa nối model: %s" % e)
        except Exception as e:  # lỗi gọi model (hết lượt, sai key, mất mạng)
            result, failure = None, (502, "%s: %s" % (type(e).__name__, str(e)[:200]))
        summary, events = tracing.end()
        drafts = list(_drafts)
        sessions = [dict(s, thu=agent.fmt_day(s["ngay"]), cap_nhat=agent.fmt_update(s["bang_cap_nhat"]))
                    for s in _sessions]
    if failure:
        return failure[0], {"error": failure[1], "steps": _steps(events)}
    output = result.get("output", "") if isinstance(result, dict) else str(result)
    summary["latency_s"] = round(time.perf_counter() - t0, 2)
    return 200, {"output": output,
                 "hoi_lai": output.rstrip().endswith("?"),  # câu do code soạn để hỏi lại (câu của model không có "?")
                 "drafts": drafts, "sessions": sessions, "steps": _steps(events), "meta": summary}


class Handler(BaseHTTPRequestHandler):
    """Dùng cho cả http.server ở máy mình lẫn hàm Python trên Vercel (api/answer.py)."""

    def _send(self, status, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path in ("/", "/index.html"):
            with open(INDEX, "rb") as f:
                return self._send(200, f.read(), "text/html; charset=utf-8")
        if path.rstrip("/") == "/api/answer":
            return self._send(200, info())
        return self._send(404, {"error": "Không có trang này."})

    def do_POST(self):
        if self.path.split("?", 1)[0].rstrip("/") != "/api/answer":
            return self._send(404, {"error": "Không có trang này."})
        try:
            n = int(self.headers.get("Content-Length") or 0)
            body = json.loads(self.rfile.read(min(n, 64 * 1024)).decode("utf-8") or "{}")
            text = body.get("text", "") if isinstance(body, dict) else ""
        except (ValueError, UnicodeDecodeError):
            return self._send(400, {"error": "Dữ liệu gửi lên không phải JSON."})
        status, res = ask(text if isinstance(text, str) else "")
        return self._send(status, res)

    def log_message(self, fmt, *args):  # không in câu hỏi của người dùng ra log
        pass
