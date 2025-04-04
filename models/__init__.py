from peewee import *
from .base import database

from .course import Course
from .user import User
from .teacher import Teacher

def create_tables():
    with database:
        database.create_tables([
            Course,
            User,
            Teacher
        ])