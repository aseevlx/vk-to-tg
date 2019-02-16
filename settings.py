import logging

BOT_API_TOKEN = ''  # token from @BotFather
TG_CHAT_ID = ''  # telegram group name

VK_APP_ID = 0  # vk app id
VK_SERVICE_TOKEN = ''  # vk service app token
VK_PAGE_ID = ''  # vk group id for tracking
POSTS_COUNT = 20  # count of posts will fetched by every iteration

PARSING_INTERVAL = 5*60  # time to sleep after every iteration

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('./logs/app.log'),
        logging.StreamHandler()
    ]
)
