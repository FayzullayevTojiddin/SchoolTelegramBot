from peewee import *
from .base import BaseModel
from .login import Login

class Student(BaseModel):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    father_name = CharField(max_length=100)
    birthday = DateField()
    description = TextField(null=True)
    login = ForeignKeyField(Login, backref='student', on_delete='SET NULL', null=True)
    status = BooleanField(default=True)