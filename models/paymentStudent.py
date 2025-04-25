from peewee import *
from .base import BaseModel
from .student import Student

class PaymentStudent(BaseModel):
    login = ForeignKeyField(Student, backref='payments', on_delete='SET NULL', null=True)
    price = IntegerField()
    description = TextField(null=True)

    class Meta():
        table_name = 'paymentstudents'