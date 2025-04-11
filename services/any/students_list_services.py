
from helpers.student.get_group_list import (
    check_join_student, get_group
)

from helpers.student.get_students_list import (
    get_students_list as get_students_list_helper, get_students_message
)

from helpers.student.get_student import (
    is_me_student, get_student, get_student_id
)

from helpers.student.get_my_profile import (
    get_student_profile_message, get_student_profile
)

from keyboards.index_keyboars import (
    students_list_keyboard
)

from keyboards.inline_keyboards import write_message_to_student_keyboard

from locales.message import get_student_message

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
            print(error)
            return False
    else:
        return False
    
def select_student_message(callback):
    student_id = callback.data.split("student:")[1]
    student = get_student(student_id)
    if is_me_student(callback):
        text = get_student_profile_message(student)
        keyboard = None
        state = None
    else:
        text = get_student_message(student)
        keyboard = write_message_to_student_keyboard(student)
        state = None
    
    return text, keyboard, state