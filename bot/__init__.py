import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "29390803"))
    API_HASH = os.environ.get("API_HASH", "4227e730acf4483f59ad2799c2bd063f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5993962044:AAHF2H0JETQxwbKeb-ugcJyCAJr2FSQRfUo")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Snapchatstoriesdownloaderbot")
    AUTH_USER = int(os.environ.get("AUTH_USER", 1383315175))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
