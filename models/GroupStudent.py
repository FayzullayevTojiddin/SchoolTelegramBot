from peewee import *
from .base import BaseModel
from .student import Student
from .group import Group

class GroupStudent(BaseModel):
    id = AutoField()
    student = ForeignKeyField(Student, backref='groups', on_delete='CASCADE')
    group = ForeignKeyField(Group, backref='students', on_delete='CASCADE')
    created_at = TimestampField()