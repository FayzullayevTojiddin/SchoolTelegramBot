from peewee import *
from models.base import BaseModel
from models.teacher import Teacher

class Course(BaseModel):
    id = AutoField()
    name = CharField()
    description = TextField()
    price = IntegerField()
    duration = CharField()
    teacher = ForeignKeyField(Teacher, backref='courses', on_delete='SET NULL', null=True)
    status = BooleanField()
    created_at = TimestampField()

    @classmethod
    def get_teacher(cls, course_id):
        try:
            course = cls.get_or_none(cls.id ==course_id)
            return course.teacher
        except:
            return False