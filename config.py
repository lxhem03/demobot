import os, time, re
import os
from typing import List

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") # ⚠️ Required
    IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Enable Force Subscribe
    AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "").split())) # Add Multiple channel id
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '')) # ⚠️ Required
    DUMP_CHANNEL = int(os.environ.get('DUMP_CHANNEL', ''))
    
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
