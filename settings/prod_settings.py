from telegram import Bot

from base_settings import *

PARSING_INTERVAL = 5*60  # time to sleep after every iteration
bot = Bot(token=BOT_API_TOKEN)
