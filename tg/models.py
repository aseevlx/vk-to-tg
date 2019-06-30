from peewee import Model, ForeignKeyField, CharField, DateTimeField, BooleanField

from settings import db
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
    date_added = DateTimeField()


class TgPost(BaseModel):
    """
    Tg post model
    """
    # url = CharField()
    #
    # sent = BooleanField()
    # date_sent = DateTimeField()
    #
    # public = ForeignKeyField(TgChannel, backref='posts')
    # vk_post = ForeignKeyField(VkPost, backref='tg_post')

    post_id = CharField()  # unique identifier of vk post
    url = CharField()

    pictures = CharField()  # picture urls, separated by comma
    text = CharField()
    reposted_from = CharField()
    reposted_text = CharField()

    sent = BooleanField()

    vk_public = ForeignKeyField(VkPublic, backref='posts')
    tg_channel = ForeignKeyField(TgChannel, backref='posts')

    date_added = DateTimeField()