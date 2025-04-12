
from peewee import ModelSelect
from models.login import Login
from models.user import User
from models.teacher import Teacher

from helpers.student.get_student import get_student

def get_login(login_id):
    return Login.get_by_id(login_id)

def get_first_name(login_id):
    login = get_login(login_id)
    role = login.role
    related_obj = getattr(login, role, None)

    if isinstance(related_obj, ModelSelect):
        related_obj = related_obj.first()

    return related_obj.first_name if related_obj else "Noma'lum foydalanuvchi"

def get_login_by_student_id(student_id):
    student = get_student(student_id)
    return student.login.id

def get_login_by_teacher_id(teacher_id):
    teacher = Teacher.get_by_id(teacher_id)
    return teacher.login_id

def get_login_by_chat_id(chat_id):
    try:
        user = User.get_user(chat_id)
        return user.login.id
    except Exception as error:
        print(error)
        return False