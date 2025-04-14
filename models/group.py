from peewee import *
from .base import BaseModel
from .teacher import Teacher
from .course import Course

class Group(BaseModel):
    teacher_id = ForeignKeyField(Teacher, backref='groups', on_delete='SET NULL', null=True)
    course_id = ForeignKeyField(Course, backref='groups', on_delete='SET NULL', null=True)
    name = CharField(max_length=100)

    @classmethod
    def getGroupById(cls, group_id: int):
        return cls.get_by_id(group_id)
    
    @classmethod
    def getHomeWorks(cls, group_id: int):
        group = cls.getGroupById(group_id)
        return group.homeworks.select()