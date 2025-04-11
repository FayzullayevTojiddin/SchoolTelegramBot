
from helpers.student.get_group_list import check_join_student

from keyboards.student_keyboards import (
    show_group_keyboard
)

from keyboards.about_keyboards import back_to_group_keyboard

from helpers.student.get_group_list import (
    get_group_message, get_group as group_in, open_group_message
)

from states.student import StudentMain

from models.teacher import Teacher

def show_group(student_id, group_id):
    checkStudent = check_join_student(student_id, group_id)
    if checkStudent:
        keyboard = show_group_keyboard(group_id, student_id)
        text = open_group_message(group_id)
        state = None
        return text, keyboard, state
    else:
        return False

def get_group(student_id, group_id):
    checkStudent = check_join_student(student_id, group_id)
    if checkStudent:
        group = group_in(group_id)
        teacher = Teacher.get_by_id(group.teacher_id)
        students = group.students.select()
        text = get_group_message(
            group.name, group.id, teacher.full_name, len(students)
        )
        keyboard = back_to_group_keyboard(group_id)
        state = None
        return text, keyboard, state
    else:
        return False