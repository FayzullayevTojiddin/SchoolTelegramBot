from aiogram import Bot

from models.user import User

from locales.message import (
    back_to_main_message_guest, 
    not_found_messsage, 
    back_to_courses_list_message, 
    cancel_write_feedback_message,
    back_to_teachers_message
)

from keyboards.inline_keyboards import (
    list_course_keyboard, 
    main_keyboard,
    list_teacher_keyboard
)

from states.any_states import (
    CourseState, MainState, TeacherState
)

def get_back_response(bot: Bot, request, user_id: int):
    role = User.get_role(user_id)
    try:
        return responses_from_role(role, request)
    except:
        return False

def responses_from_role(role, request):
    if role == 'guest':
        return get_request_from_guest(request)
    elif role == 'teacher':
        pass
    elif role == 'admin':
        pass
    else:
        return False
    
def get_request_from_guest(request):
    if request == 'main':
        message = back_to_main_message_guest
        keyboard = main_keyboard()
        state = MainState.main
    elif request == 'courses':
        message = back_to_courses_list_message
        keyboard = list_course_keyboard()
        state = CourseState.main
    elif request == 'feedbacks':
        message = cancel_write_feedback_message
        keyboard = main_keyboard()
        state = MainState.main
    elif request == 'teachers':
        message = back_to_teachers_message
        keyboard = list_teacher_keyboard()
        state = TeacherState.main
    else:
        message = not_found_messsage
        keyboard = None
        state = None

    return message, keyboard, state