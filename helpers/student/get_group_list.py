from models.user import User
from models.student import Student

def get_groups(user_id):
    user = User.get_user(user_id)
    if not user or not user.login:
        return []

    student = Student.get_or_none(Student.login == user.login)
    if not student:
        return []

    return [gs.group for gs in student.groups]