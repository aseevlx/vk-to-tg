import logging
import os

from dotenv import load_dotenv
from peewee import SqliteDatabase

load_dotenv()

BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')
TG_CHAT_ID = os.getenv('TG_CHAT_ID')
VK_APP_ID = int(os.getenv('VK_APP_ID'))
VK_SERVICE_TOKEN = os.getenv('VK_SERVICE_TOKEN')
VK_PAGE_ID = os.getenv('VK_PAGE_ID')
POSTS_COUNT = int(os.getenv('POSTS_COUNT'))
DB_PATH = os.getenv('DB_PATH')

db = SqliteDatabase(DB_PATH)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('./logs/app.log'),
        logging.StreamHandler()
    ]
)
