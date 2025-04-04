from locales.message import (
    courses_message, teachers_message, feedbak_message, login_message
)

from keyboards.inline_keyboards import (
    list_course_keyboard, list_teacher_keyboard
)

from states.any_states import (
    CourseState, TeacherState
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
        pass
    elif request == 'login':
        pass
    else:
        return False
    
    return keyboard, text, state