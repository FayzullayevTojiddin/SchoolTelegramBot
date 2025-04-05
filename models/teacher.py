from peewee import *
from .base import BaseModel

class Teacher(BaseModel):
    id = AutoField()
    user_id = BigIntegerField(unique=True)
    phone_number = CharField(max_length=13)
    telegram = CharField(max_length=50)
    full_name = CharField(max_length=100)
    subject = CharField(max_length=50)
    experience = CharField(max_length=100)
    school = CharField(max_length=50)
    achievements = CharField(max_length=200)
    feedback = CharField(max_length=100)
    description = CharField(max_length=1000)
    created_at = TimestampField()

    @classmethod
    def get_courses(cls, teacher_id):
        try:
            teacher = cls.get_or_none(cls.id == teacher_id)
            if teacher:
                return [ct.course for ct in teacher.courses]
            return []
        except:
            return []