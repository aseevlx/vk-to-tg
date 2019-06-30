from vk.models import VkPublic
from tg.models import TgPost, TgChannel, db


def create_tables():
    with db:
        db.create_tables([VkPublic, TgChannel, TgPost])
