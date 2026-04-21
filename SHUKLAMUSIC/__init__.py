# -----------------------------------------------
# 🔸 StrangerMusic Project
# 🔹 Developed & Maintained by: Shashank Shukla (https://github.com/itzshukla)
# 📅 Copyright © 2022 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItzShukla
# -----------------------------------------------

import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from SHUKLAMUSIC.core.bot import SHUKLA
from SHUKLAMUSIC.core.dir import dirr
from SHUKLAMUSIC.core.git import git
from SHUKLAMUSIC.core.userbot import Userbot
from SHUKLAMUSIC.misc import dbb, heroku
from SafoneAPI import SafoneAPI
from .logging import LOGGER


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  KEEP-ALIVE — Thread mein chalata hai (asyncio se pehle)
#  http.server use kiya — koi extra library nahi chahiye
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class _Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h2>StrangerMusic Bot is running!</h2>")

    def log_message(self, format, *args):
        pass   # suppress access logs


def _start_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), _Handler)
    LOGGER("KeepAlive").info(f"Server started on port {port} ✅")
    server.serve_forever()


# Thread mein start karo — asyncio loop ka wait nahi
_thread = threading.Thread(target=_start_server, daemon=True)
_thread.start()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  ORIGINAL __init__.py — bilkul same
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

dirr()
git()
dbb()
heroku()

app      = SHUKLA()
userbot  = Userbot()
api      = SafoneAPI()

from .platforms import *

Apple      = AppleAPI()
Carbon     = CarbonAPI()
SoundCloud = SoundAPI()
Spotify    = SpotifyAPI()
Resso      = RessoAPI()
Telegram   = TeleAPI()
YouTube    = YouTubeAPI()

APP = "InflexOwnerBot"  # connect music api key "Dont change it"
