from peewee import *
from .base import BaseModel
from .group import Group

class HomeWork(BaseModel):
    id = AutoField()
    group_id = ForeignKeyField(Group, backref='homeworks', on_delete='CASCADE')
    completed = BooleanField(default=False)
    title = CharField(max_length=100)
    description = TextField(null=True)
    created_at = TimestampField()