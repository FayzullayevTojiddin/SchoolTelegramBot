from peewee import *
from .base import BaseModel

class Feedback(BaseModel):
    id = AutoField()
    user_id = BigIntegerField()
    question = CharField(max_length=1000)