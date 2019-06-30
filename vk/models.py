from peewee import Model, CharField, DateTimeField

from settings import db


class BaseModel(Model):
    class Meta:
        database = db


class VkPublic(BaseModel):
    """
    VK public model
    """
    vk_id = CharField()
    name = CharField()
    url = CharField()
    date_added = DateTimeField()
