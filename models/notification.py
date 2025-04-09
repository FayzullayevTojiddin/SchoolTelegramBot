from peewee import *
from .base import BaseModel
from .user import User
from .login import Login

class Notification(BaseModel):
    id = AutoField()
    from_in = ForeignKeyField(Login, backref='sended_notifications', on_delete='CASCADE')
    to = ForeignKeyField(User, backref='notifications', on_delete='CASCADE')
    message = TextField()
    hidden = BooleanField(default=False)
    readed = BooleanField(default=False)
    created_at = TimestampField()