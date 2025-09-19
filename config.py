import os, time, re
import os
from typing import List

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "23898744")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "0b13c810c80b548604650cbe3c3db0c3") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6912498692:AAH0lO6ul6FdyrOG0Nh6uzKsImhFwZrGZWI") # ⚠️ Required
    IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Enable Force Subscribe
    AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-100xxxxxxxxx -100xxxxxxx").split())) # Add Multiple channel id
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://filmyrohesh51:19SmDYqC1N5DqLkD@cluster0.jogzc68.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "5698613889")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002077680328')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/15e82d7e665eccc8bd9c5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
