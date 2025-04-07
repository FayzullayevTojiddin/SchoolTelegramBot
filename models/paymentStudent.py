from peewee import *
from .base import BaseModel
from .student import Student

class PaymentStudent(BaseModel):
    id = AutoField()
    login = ForeignKeyField(Student, backref='payments', on_delete='SET NULL', null=True)
    price = IntegerField()
    description = TextField(null=True)
    created_at = TimestampField()