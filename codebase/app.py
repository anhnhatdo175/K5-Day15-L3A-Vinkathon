"""Bản chạy thử: giao diện web (mặc định) hoặc dòng lệnh. Cả hai gọi answer() trong agent.py.

Chạy bằng: python run.py   (macOS/Linux có thể là python3, Windows có thể là py)
  → mở http://localhost:8000 (cổng bận thì thử 8001…; đặt cổng khác: biến môi trường PORT)
Bản dòng lệnh cũ: python codebase/app.py --cli
Bản trên Vercel dùng cùng code giao diện (codebase/web.py, public/index.html) qua api/answer.py.
"""
import os
import sys

for _stream in (sys.stdout, sys.stderr, sys.stdin):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def _where(e):
    """File (trong codebase/) gây lỗi khi nạp: SyntaxError có e.filename, lỗi khác lấy khung cuối của traceback."""
    import traceback
    path = getattr(e, "filename", None) or (traceback.extract_tb(e.__traceback__)[-1].filename if e.__traceback__ else "")
    if not path:
        return "codebase/"
    p = os.path.abspath(path)
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.relpath(p, base).replace(os.sep, "/") if p.startswith(base) else path


def _load_error(e):
    print("Không nạp được codebase/ — lỗi ở %s: %s: %s" % (_where(e), type(e).__name__, e))
    print("Sửa lỗi rồi chạy lại. Cách nối model: docs/connect-model.md")
    return 1


def web(open_browser=True) -> int:
    try:
        import web as webui
    except Exception as e:  # lỗi cú pháp, thiếu thư viện… trong codebase/
        return _load_error(e)
    from http.server import ThreadingHTTPServer

    start = int(os.environ.get("PORT") or 8000)
    server = None
    for port in range(start, start + 10):
        try:
            server = ThreadingHTTPServer(("127.0.0.1", port), webui.Handler)
            break
        except OSError:
            continue
    if server is None:
        print("Không mở được cổng %d–%d. Đặt cổng khác: PORT=9000 python run.py" % (start, start + 9))
        return 1
    url = "http://localhost:%d" % server.server_address[1]
    i = webui.info()
    print("Bản chạy thử (web) đang chạy ở %s · model: %s" % (url, i["model"]))
    print("Thoát: Ctrl+C. Bản dòng lệnh: python codebase/app.py --cli")
    if open_browser:
        try:
            import webbrowser
            webbrowser.open(url)
        except Exception:
            pass
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print()
    finally:
        server.server_close()
    return 0


def cli() -> int:
    try:
        import tracing
        from agent import answer
    except Exception as e:  # lỗi cú pháp, thiếu thư viện… trong codebase/
        return _load_error(e)
    print("Bản chạy thử — gõ đầu vào rồi Enter. Thoát: Ctrl+C (hoặc Enter 2 lần với dòng trống).")
    blank = 0
    while True:
        try:
            text = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if not text:
            blank += 1
            if blank >= 2:
                return 0
            continue
        blank = 0
        tracing.begin("app")
        try:
            result = answer(text)
        except NotImplementedError as e:
            tracing.end()
            print("Chưa nối model: %s" % e)
            return 1
        except Exception as e:  # lỗi gọi model: báo rồi cho hỏi tiếp
            tracing.end()
            print("[lỗi] %s: %s" % (type(e).__name__, e))
            continue
        s, _ = tracing.end()
        print(result.get("output", "") if isinstance(result, dict) else result)
        print("   (model: %s · gọi model %d lần · công cụ %d lần · token vào %d / ra %d)"
              % (", ".join(s["models"]) or "—", s["model_calls"], s["tool_calls"], s["tokens_in"], s["tokens_out"]))


def main() -> int:
    if "--cli" in sys.argv[1:]:
        return cli()
    return web(open_browser="--no-browser" not in sys.argv[1:])


if __name__ == "__main__":
    sys.exit(main())
