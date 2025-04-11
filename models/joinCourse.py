from peewee import *
from .base import BaseModel
from models.user import User
from models.course import Course

class JoinCourse(BaseModel):
    user = ForeignKeyField(User, backref='joined_courses', on_delete='CASCADE', field='user_id')
    course = ForeignKeyField(Course, backref='joined_users', on_delete='CASCADE')

    @classmethod
    def check_join(cls, user_id, course_id):
        join = cls.select().where(cls.user == user_id, cls.course == course_id).first()
        if join:
            return True
        return False
    
    @classmethod
    def join(cls, user_id, course_id):
        if cls.check_join(user_id, course_id):
            return True
            
        try:
            return cls.create(user=user_id, course=course_id)
        except Exception as e:
            print(e)
            return False