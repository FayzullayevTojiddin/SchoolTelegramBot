from peewee import *
from .base import BaseModel
from .user import User
from .login import Login

class Notification(BaseModel):
    from_in = ForeignKeyField(Login, backref='sended_notifications', on_delete='CASCADE')
    to = ForeignKeyField(Login, backref='notifications', on_delete='CASCADE')
    message = TextField()
    hidden = BooleanField(default=False)
    read = BooleanField(default=False)