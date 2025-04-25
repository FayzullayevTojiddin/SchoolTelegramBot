from peewee import *
from .base import BaseModel

from .course import Course
from .teacher import Teacher

class CourseTeacher(BaseModel):
    course = ForeignKeyField(Course, backref='teachers')
    teacher = ForeignKeyField(Teacher, backref='courses')

    class Meta():
        table_name = 'courseteachers'