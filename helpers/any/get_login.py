
from peewee import ModelSelect
from models.login import Login

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