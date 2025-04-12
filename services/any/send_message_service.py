
from helpers.student.get_student import is_me_student

from locales.message import (
    this_student_you, get_message_to_send, message_is_not_text_error, message_sent_successfully
)

from keyboards.cancel_ceyboards import cancel_message_keyboard

from helpers.get_main_keyboard_helper import get_main_keyboard
from helpers.any.send_notification_helpers import send_notification
from helpers.any.get_login import (
    get_login_by_chat_id, get_login_by_student_id, get_login_by_teacher_id
)

from states.any_states import (
    SendMessage, MainState
)

async def send_message_request_to_response(callback, old_state):
    callback_data = callback.data.split(":")
    to_id = callback_data[1]
    from_type = callback_data[0]
    if from_type == 'write-message' and is_me_student(callback):
        text = this_student_you
        keyboard = None
        state = old_state
    else:
        text = get_message_to_send
        keyboard = cancel_message_keyboard()
        state = SendMessage.get_message

    await old_state.update_data(to_id=to_id, from_type=from_type)
    return text, keyboard, state

async def send_message_to(message, state):
    datas = await state.get_data()
    from_in = get_login_by_chat_id(message.from_user.id)
    from_type = datas['from_type']
    if from_type == 'write-message':
        student_id = datas['to_id']
        from_to = get_login_by_student_id(student_id)
    elif from_type == 'write-teacher':
        teacher_id = datas['to_id']
        from_to = get_login_by_teacher_id(teacher_id)

    if message.text:
        send_notification(from_in, from_to, message.text)
        text = message_sent_successfully
        keyboard = get_main_keyboard('student')
        state = MainState.main
    else:
        text = message_is_not_text_error
        keyboard = cancel_message_keyboard()
        state = SendMessage.get_message

    return text, keyboard, state