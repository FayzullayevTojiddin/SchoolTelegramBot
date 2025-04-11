from models.user import User
from models.student import Student
from models.GroupStudent import GroupStudent
from models.group import Group

def get_groups(user_id):
    user = User.get_user(user_id)
    if not user or not user.login:
        return []

    student = Student.get_or_none(Student.login == user.login)
    if not student:
        return []

    return [gs.group for gs in student.groups]


def check_join_student(student_id, group_id):
    return GroupStudent.select().where(
        (GroupStudent.student_id == student_id) &
        (GroupStudent.group_id == group_id)
    ).exists()

def get_group_message(groupName, groupId, teacherName, studentCounts):
    return f"""
ℹ️ Guruh haqida

📘 Nomi: {groupName}
🆔 Guruh ID: {groupId}

👨‍🏫 O‘qituvchi(lar): 
- {teacherName}

👥 O‘quvchilar soni: {studentCounts} ta"""

def get_group(group_id):
    return Group.get_by_id(group_id)

def open_group_message(group_id):
    return f"""🎉 Siz guruhga muvaffaqiyatli kirdingiz!

Guruh ID: {group_id}

Endi siz guruhdagi barcha faoliyatlarni kuzatib borishingiz mumkin!
"""