
from locales.message import (
    back_to_main_message
)

from helpers.get_main_keyboard_helper import get_main_keyboard

from states.student import StudentMain

def get_request_from_student(request):
    role = 'student'
    if request == 'main':
        message = back_to_main_message
        keyboard = get_main_keyboard(role)
        state = StudentMain.main

    return message, keyboard, state