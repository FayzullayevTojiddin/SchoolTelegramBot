from peewee import *
from .base import BaseModel
from .login import Login

class User(BaseModel):
    user_id = BigIntegerField(unique=True)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255, null=True)
    username = CharField(max_length=100, null=True)
    role = CharField(max_length=10, default="guest")
    is_register = BooleanField(default=False)
    full_name = CharField(null=True)
    age = IntegerField(null=True)
    phoneNumber = CharField(null=True)
    login = ForeignKeyField(Login, backref='users', on_delete='SET NULL', null=True)

    @classmethod
    def get_role(cls, user_id):
        return cls.get_or_none(cls.user_id == user_id).role
    
    @classmethod
    def get_user(cls, user_id):
        return cls.get_or_none(cls.user_id == user_id)
    
    @classmethod
    def registerUser(cls, user_id, full_name, age, phoneNumber):
        user = cls.get_user(user_id)
        user.phoneNumber = phoneNumber
        user.age = age
        user.full_name = full_name
        user.is_register = True
        user.save()

    class Meta():
        table_name = "telegram_users"