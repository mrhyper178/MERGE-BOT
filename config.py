import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "f19aed00b0c74abed0359016afc1733f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6855063215:AAEBzl6S1kegerTv-jyUgP4Q_PdKqtU5G74")
    TELEGRAM_API = 8733404
    OWNER = os.environ.get("OWNER", "807374433")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "NewUserExist")
    PASSWORD = os.environ.get("PASSWORD", "asuran")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://leecher:leecher@cluster0.606mkpi.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1001547137091")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "AQAaiBkAt9DsH8XO1z9_dxUkBgcLvnAKii6M9A5uFZi3coeUdFVTOPfNzMqjv6PGUgQa3hoE4uAkyEh7E531j1mGHxNBk8b9NSIV0KibnhJLVGsullkw5ge1H_qUoBCLzy3XHC1J_a9SfEu_5j_41cv82B-Ee1D-gF5luTdMe8W2-m77o8JDS8z1zUwS8zgYMyFy7ZSaoC7u49U8YCBARbaRhxThWwcJVtboFgv-BGacEiMYDtU-xHvgX4Zu1TkYLaz_9neSp4Tt__MYGIt8xttL5qYIYWJz42z_agyB0ktWzIujAU-LF7KTn5zVLq4xh-A3WSih4yitslDc2DvCty_GEAcRgwAAAABRsDH9AA")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
