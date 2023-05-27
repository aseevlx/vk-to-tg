import logging
import os

from dotenv import load_dotenv
from peewee import SqliteDatabase
from telegram import Bot

load_dotenv()

BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")
VK_APP_ID = int(os.getenv("VK_APP_ID"))
VK_SERVICE_TOKEN = os.getenv("VK_SERVICE_TOKEN")
VK_PAGE_ID = int(os.getenv("VK_PAGE_ID"))
POSTS_COUNT = int(os.getenv("POSTS_COUNT"))
DB_PATH = os.getenv("DB_PATH")

TG_CHANNEL_NAME = os.getenv("TG_CHANNEL_NAME")
TG_CHANNEL_URL = os.getenv("TG_CHANNEL_URL")
VK_PUBLIC_NAME = os.getenv("VK_PUBLIC_NAME")
VK_PUBLIC_URL = os.getenv("TG_CHANNEL_URL")

db = SqliteDatabase(DB_PATH)

bot = Bot(token=BOT_API_TOKEN)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    handlers=[logging.FileHandler("./logs/app.log"), logging.StreamHandler()],
)
