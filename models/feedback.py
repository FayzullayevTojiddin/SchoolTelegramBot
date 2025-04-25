from peewee import *
from .base import BaseModel

class Feedback(BaseModel):
    user_id = BigIntegerField()
    question = CharField(max_length=1000)

    class Meta():
        table_name = 'feedbacks'