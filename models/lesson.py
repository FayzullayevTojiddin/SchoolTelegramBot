from peewee import *

from .base import BaseModel
from .group import Group

from enum import IntEnum

class LessonStatus(IntEnum):
    PLANNED = 0
    COMPLETED = 1
    CANCELLED = 2

class Lesson(BaseModel):
    id = AutoField()
    name = CharField(max_length=255)
    group = ForeignKeyField(Group, backref='lessons', on_delete='CASCADE')
    time_in = TimeField()
    time_to = TimeField()
    date = DateField()
    status = IntegerField(default=LessonStatus.PLANNED)
    created_at = TimestampField()