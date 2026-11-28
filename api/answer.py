"""Hàm Python trên Vercel: /api/answer → codebase/web.py (cùng code với `python run.py` ở máy mình).

Model chọn bằng biến môi trường của project trên Vercel (MODEL_PROVIDER, MODEL_NAME, API_KEY), không đọc .env.
Chưa đặt biến thì chạy chế độ giả.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "codebase"))

import web  # noqa: E402


class handler(web.Handler):
    pass
