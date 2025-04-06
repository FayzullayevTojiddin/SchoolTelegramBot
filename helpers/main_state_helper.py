from locales.message import (
    courses_message, teachers_message, feedbak_message, login_message
)
from keyboards.inline_keyboards import (
    list_course_keyboard, list_teacher_keyboard, cancel_feedback_keyboard, main_keyboard
)

from locales.keyboard import (
    teacher_panel_keyboard, admin_panel_keyboard, student_panel_keyboard
)

from keyboards.main_keyboards import main_keyboards

from keyboards.cancel_ceyboards import cancel_login_keyboard

from states.any_states import (
    CourseState, TeacherState, FeedbakState, LoginState
)

def main_state_response(request):
    if request == 'courses':
        keyboard = list_course_keyboard()
        text = courses_message
        state = CourseState.main
    elif request == 'teachers':
        keyboard = list_teacher_keyboard()
        text = teachers_message
        state = TeacherState.main
    elif request == 'feedbacks':
        keyboard = cancel_feedback_keyboard()
        text = feedbak_message
        state = FeedbakState.main
    elif request == 'login':
        keyboard = cancel_login_keyboard()
        text = login_message
        state = LoginState.login
    else:
        return False
    
    return keyboard, text, state

def get_main_keyboard(role):
    if role == 'student':
        keyboard = main_keyboards(student_panel_keyboard)
    elif role == 'admin' :
        keyboard = main_keyboards(admin_panel_keyboard)
    elif role == 'teacher' :
        keyboard = main_keyboards(teacher_panel_keyboard)
    elif role == 'guest' :
        keyboard = main_keyboard()

    return keyboard