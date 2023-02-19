# (c) @JigarVarma2005

import os


class Config(object):
    # get it from my.telegram.org
    APP_ID = os.environ.get("APP_ID", 3343389)
    API_HASH = os.environ.get("API_HASH", "3a20ed9427d8b5c50577c99212e9380b")
    # Get it from @botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6024285748:AAFqFR92Vt3EmBwtZWDR3vMXWcNAEOf1h1k")
    # Leave this defualt
    SESSION_NAME = os.environ.get("SESSION_NAME", "Captcha_iBot")
    # get it from https://cloud.mongodb.com 
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://tgcaptchabot:tgcaptchabot@cluster0.dbnft3n.mongodb.net/?retryWrites=true&w=majority")
    # Ask in https://t.me/JV_Community
    API_TOKEN = os.environ.get("API_TOKEN", None)
    # Sudo users(goto @JVToolsBot and send /id to get your id)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1496092965 1204927413 1405957830").split()))
    SUDO_USERS.append(1204927413)
    SUDO_USERS = list(set(SUDO_USERS))
