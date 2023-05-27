from settings import db, TG_CHAT_ID, TG_CHANNEL_NAME, TG_CHANNEL_URL, VK_PAGE_ID, POSTS_COUNT, VK_PUBLIC_NAME
from tg.models import TgPost, TgChannel
from vk.models import VkPublic


def create_tables():
    with db:
        db.create_tables([VkPublic, TgChannel, TgPost])
    fill_db()


def fill_db():
    TgChannel(chat_id=TG_CHAT_ID, name=TG_CHANNEL_NAME, url=TG_CHANNEL_URL).save()
    VkPublic(page_id=VK_PAGE_ID, posts_count=POSTS_COUNT, name=VK_PUBLIC_NAME, url=TG_CHANNEL_URL).save()
