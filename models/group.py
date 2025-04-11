from peewee import *
from .base import BaseModel
from .teacher import Teacher
from .course import Course

class Group(BaseModel):
    teacher_id = ForeignKeyField(Teacher, backref='groups', on_delete='SET NULL', null=True)
    course_id = ForeignKeyField(Course, backref='groups', on_delete='SET NULL', null=True)
    name = CharField(max_length=100)