from peewee import *
from models.base import BaseModel

class Course(BaseModel):
    id = AutoField()
    name = CharField()
    description = BigIntegerField()
    created_at = TimestampField