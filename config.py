import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7944481456:AAHk5ZtiFHM0bmDr8esFIFC5hg8P2GyO6a4")
APP_ID = int(os.environ.get("APP_ID", "7236453"))
API_HASH = os.environ.get("API_HASH", "33010a70e94f80e55145980072cce969")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002319985549"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6891428437"))
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://videshi:videshi@videshi.wtffv.mongodb.net/?retryWrites=true&w=majority&appName=videshi")
DB_NAME = os.environ.get("DATABASE_NAME", "codeflix_bots")

#Shortner (token system) 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "modijiurl.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "36ac726770f0492bb40f1ac8144703c49fdef866")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/howtoopen88/6") 

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002231278815"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝖧𝖾𝗅𝗅𝗈 👋 {first}, 𝖳𝗁𝖺𝗇𝗄𝗌 𝖥𝗈𝗋 𝖴𝗌𝗂𝗇𝗀 𝖬𝖾 :𝖣  ⚡️.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6891428437").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "𝘛𝘩𝘪𝘴 𝘷𝘪𝘥𝘦𝘰/𝘗𝘩𝘰𝘵𝘰/𝘢𝘯𝘺𝘵𝘩𝘪𝘯𝘨 𝘪𝘴 𝘢𝘷𝘢𝘪𝘭𝘢𝘣𝘭𝘦 𝘰𝘯 𝘵𝘩𝘦 𝘪𝘯𝘵𝘦𝘳𝘯𝘦𝘵. 𝘞𝘦 𝘰𝘳 𝘪𝘵𝘴 𝘴𝘶𝘣𝘴𝘪𝘥𝘪𝘢𝘳𝘺 𝘤𝘩𝘢𝘯𝘯𝘦𝘭 𝘥𝘰𝘦𝘴𝘯'𝘵 𝘱𝘳𝘰𝘥𝘶𝘤𝘦 𝘢𝘯𝘺 𝘰𝘧 𝘵𝘩𝘦𝘮☀︎︎")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!🥱"

ADMINS.append(OWNER_ID)
ADMINS.append(6891428437)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
