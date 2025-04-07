from peewee import *
from .base import BaseModel
from .teacher import Teacher
from .course import Course

class Group(BaseModel):
    id = AutoField()
    teacher_id = ForeignKeyField(Teacher, backref='groups', on_delete='SET NULL', null=True)
    course_id = ForeignKeyField(Course, backref='groups', on_delete='SET NULL', null=True)