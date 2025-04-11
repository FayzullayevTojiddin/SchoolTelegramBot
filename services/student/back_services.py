
from locales.message import (
    back_to_main_message, get_message_canel_to_send
)

from helpers.get_main_keyboard_helper import get_main_keyboard

from helpers.student.get_group_list import get_groups

from keyboards.student_keyboards import get_groups_keyboard

from locales.message import list_groups_message_student

from states.student import (
    StudentMain, StudentGroups
)

def get_request_from_student(callback):
    request = callback.data.split(":")[1]
    role = 'student'
    if request == 'main':
        message = back_to_main_message
        keyboard = get_main_keyboard(role)
        state = StudentMain.main
    elif request == 'groups':
        groups = get_groups(callback.from_user.id)
        keyboard = get_groups_keyboard(groups)
        message = list_groups_message_student
        state = StudentGroups.main
    elif request == 'message':
        message = get_message_canel_to_send
        keyboard = get_main_keyboard(role)
        state = StudentMain.main

    return message, keyboard, state