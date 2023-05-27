from datetime import datetime

from peewee import Model, CharField, DateTimeField

from settings import db


class BaseModel(Model):
    class Meta:
        database = db


class VkPublic(BaseModel):
    """
    VK public model
    """

    page_id = CharField()
    posts_count = CharField()  # how many posts fetch
    name = CharField()
    url = CharField()
    date_added = DateTimeField(default=datetime.now)
    last_check_date = DateTimeField(default=datetime.now)
