from peewee import *
from .base import BaseModel
from .group import Group

class HomeWork(BaseModel):
    group_id = ForeignKeyField(Group, backref='homeworks', on_delete='CASCADE')
    completed = BooleanField(default=False)
    title = CharField(max_length=100)
    description = TextField(null=True)

    class Meta():
        table_name = 'homeworks'
