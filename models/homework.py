from peewee import *
from .base import BaseModel
from .user import User
from .group import Group

class HomeWork(BaseModel):
    id = AutoField()
    user_id = ForeignKeyField(User, backref='homeworks', on_delete='CASCADE')
    group_id = ForeignKeyField(Group, backref='homeworks', on_delete='CASCADE')
    completed = BooleanField(default=False)
    title = CharField(max_length=100)
    description = TextField(null=True)
    created_at = TimestampField()