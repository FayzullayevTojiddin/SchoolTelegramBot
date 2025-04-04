from peewee import *
from .base import BaseModel

class Teacher(BaseModel):
    id = AutoField()
    user_id = BigIntegerField()
    phone_number = CharField(max_length=13)
    full_name = CharField(max_length=100)
    description = CharField(max_length=1000)
    created_at = TimestampField()