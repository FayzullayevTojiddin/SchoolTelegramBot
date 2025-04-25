from peewee import *
from .base import BaseModel
from .group import Group

class Material(BaseModel):
    name = CharField(max_length=255)
    path = CharField(max_length=100)
    type = CharField()
    group = ForeignKeyField(Group, backref='materials', on_delete='CASCADE')

    class Meta():
        table_name = 'materials'