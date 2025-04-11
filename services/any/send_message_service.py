
from helpers.student.get_student import is_me_student

from locales.message import (
    this_student_you, get_message_to_send, message_is_not_text_error, message_sent_successfully
)

from keyboards.cancel_ceyboards import cancel_message_keyboard
from helpers.get_main_keyboard_helper import get_main_keyboard

from states.any_states import (
    SendMessage, MainState
)

def send_message_request_to_response(callback, old_state):
    if is_me_student(callback):
        text = this_student_you
        keyboard = None
        state = old_state
    else:
        text = get_message_to_send
        keyboard = cancel_message_keyboard()
        state = SendMessage.get_message

    return text, keyboard, state

def send_message_to(message):
    if message.text:
        text = message_sent_successfully
        keyboard = get_main_keyboard('student')
        state = MainState.main
    else:
        text = message_is_not_text_error
        keyboard = cancel_message_keyboard()
        state = SendMessage.get_message

    return text, keyboard, state