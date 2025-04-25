from peewee import *
from .base import BaseModel
from .student import Student
from .group import Group

class GroupStudent(BaseModel):
    student = ForeignKeyField(Student, backref='groups', on_delete='CASCADE')
    group = ForeignKeyField(Group, backref='students', on_delete='CASCADE')
    created_at = TimestampField()

    class Meta():
        table_name = 'groupstudents'