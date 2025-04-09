
from helpers.student.get_group_list import (
    check_join_student, get_group
)

from helpers.student.get_students_list import (
    get_students_list as get_students_list_helper, get_students_message
)

from keyboards.index_keyboars import students_list_keyboard

def get_students_list(group_id, student_id):
    checkJoin = check_join_student(student_id, group_id)
    if checkJoin:
        try:
            group = get_group(group_id)
            students = get_students_list_helper(group)
            keyboard = students_list_keyboard(students, group_id)
            text = get_students_message(group_id, len(students))
            state = None
            return text, keyboard, state
        except Exception as error:
            return False
    else:
        return False