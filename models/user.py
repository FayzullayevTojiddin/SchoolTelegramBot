from peewee import *
from .base import BaseModel

class User(BaseModel):
    id = AutoField()
    user_id = BigIntegerField()
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255, null=True)
    username = CharField(max_length=100, null=True)
    role = CharField(max_length=10, default="guest")
    created_at = TimestampField()

    @classmethod
    def get_role(cls, user_id):
        return cls.get_or_none(cls.user_id == user_id).role
    
    @classmethod
    def get_user(cls, user_id):
        return cls.get_or_none(cls.user_id == user_id)