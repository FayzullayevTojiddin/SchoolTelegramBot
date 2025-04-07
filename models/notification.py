from peewee import *
from .base import BaseModel
from .user import User

class Notification(BaseModel):
    id = AutoField()
    to = ForeignKeyField(User, backref='notifications', on_delete='CASCADE')
    message = TextField()
    hidden = BooleanField(default=False)
    readed = BooleanField(default=False)
    created_at = TimestampField()