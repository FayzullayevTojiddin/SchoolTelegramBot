from peewee import *
from .base import BaseModel

class Login(BaseModel):
    login = CharField(max_length=30)
    password = CharField(max_length=50)
    role = CharField(max_length=10)

    @classmethod
    def isset_login(cls, login):
        return cls.get_or_none(cls.login == login)
    
    @classmethod
    def check_password(cls, login, password):
        login = cls.isset_login(login)
        if login:
            return login.password == password
        else:
            return True