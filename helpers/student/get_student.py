
from models.user import User
from models.student import Student

def get_student_id(user_id):
    return User.get_user(user_id).login.student.get().id

def get_student(student_id):
    return Student.get_by_id(student_id)

def is_me_student(callback):
    this_id = callback.data.split(':')[1]
    me_id = get_student_id(callback.from_user.id)
    this = get_student(this_id)
    me = get_student(me_id)
    if this == me:
        return True
    else:
        return False