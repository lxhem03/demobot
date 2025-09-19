import os, time, re
import os
from typing import List

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "27394279")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "90a9aa4c31afa3750da5fd686c410851") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7492763086:AAGKmIggAREQZHGlVAc37SR1egEw-AH6Rys") # ⚠️ Required
    IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Enable Force Subscribe
    AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002226481922").split())) # Add Multiple channel id
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://python21java:8ZFGYMKJCqAPwsiO@filestore.f876hjv.mongodb.net/?retryWrites=true&w=majority&appName=Filestore")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","TeleGuy") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "1705634892")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002355748198')) # ⚠️ Required
    DUMP_CHANNEL = int(os.environ.get('DUMP_CHANNEL', '-1002731272735'))
    
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
__**🎬 {0}**__
──────────────
**💾 Original:** __{1}__
**📦 Encoded:** __{2}__
**📉 Compression:** __{3}__
──────────────
*,⏱️ Downloaded:** __{4}__
**⏱️ Encoded:** __{5}__
**⏱️ Uploaded:** __{6}__
──────────────
"""

dump = """
__**🎬 {0}**__
──────────────
**💾 Original:** __{1}__
**📦 Encoded:** __{2}__
**📉 Compression:** __{3}__
──────────────
*,👤 Mention:** {4}
**👤 ID:** `{5}`
──────────────
"""
