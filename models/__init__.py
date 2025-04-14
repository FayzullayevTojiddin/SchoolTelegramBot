from peewee import *
from .base import database

from .course import Course
from .user import User
from .teacher import Teacher
from .joinCourse import JoinCourse
from .CourseTeacher import CourseTeacher
from .feedback import Feedback
from .login import Login
from .student import Student
from .group import Group
from .GroupStudent import GroupStudent
from .notification import Notification
from .paymentStudent import PaymentStudent
from .material import Material
from .homework import HomeWork

def create_tables():
    with database:
        database.create_tables([
            Course,
            User,
            Teacher,
            JoinCourse,
            CourseTeacher,
            Feedback,
            Login,
            Student,
            Group,
            GroupStudent,
            Notification,
            PaymentStudent,
            Material,
            HomeWork
        ])