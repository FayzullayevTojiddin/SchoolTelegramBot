from peewee import *
from .base import BaseModel

class Student(BaseModel):
    id = AutoField()
    status = BooleanField(default=True)
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    father_name = CharField(max_length=100)
    birthday = TimeField()
    description = TextField(null=True)
    created_at = TimestampField()