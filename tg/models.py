from datetime import datetime

from peewee import Model, ForeignKeyField, CharField, DateTimeField, BooleanField

from settings import db, TG_CHAT_ID
from vk.models import VkPublic


class BaseModel(Model):
    class Meta:
        database = db


class TgChannel(BaseModel):
    """
    TG channel model
    """
    chat_id = CharField()
    name = CharField()
    url = CharField()
    date_added = DateTimeField(default=datetime.now)


class TgPost(BaseModel):
    """
    Tg post model
    """
    post_id = CharField()  # unique identifier of vk post

    pictures = CharField(default='')  # picture urls, separated by comma
    text = CharField(default='')

    reposted_from = CharField(default='')
    reposted_text = CharField(default='')
    reposted_pictures = CharField(default='')  # picture urls, separated by comma

    sent = BooleanField(default=False)

    vk_public = ForeignKeyField(VkPublic, backref='posts')
    tg_channel = ForeignKeyField(TgChannel, backref='posts')

    date_added = DateTimeField(default=datetime.now)