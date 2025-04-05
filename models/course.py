from peewee import *
from models.base import BaseModel

class Course(BaseModel):
    id = AutoField()
    name = CharField()
    description = TextField()
    price = IntegerField()
    duration = CharField()
    status = BooleanField()
    created_at = TimestampField()

    @classmethod
    def get_teachers(cls, course_id):
        try:
            course = cls.get_or_none(cls.id == course_id)
            if course:
                return [ct.teacher for ct in course.teachers]
            return []
        except:
            return []