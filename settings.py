import os
import logging

from dotenv import load_dotenv

load_dotenv()

BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')
TG_CHAT_ID = os.getenv('TG_CHAT_ID')
VK_APP_ID = int(os.getenv('VK_APP_ID'))
VK_SERVICE_TOKEN = os.getenv('VK_SERVICE_TOKEN')
VK_PAGE_ID = os.getenv('VK_PAGE_ID')
POSTS_COUNT = int(os.getenv('POSTS_COUNT'))

PARSING_INTERVAL = 5*60  # time to sleep after every iteration

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('./logs/app.log'),
        logging.StreamHandler()
    ]
)
