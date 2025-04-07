from states.any_states import (
    MainState, TeacherState, CourseState
)

from keyboards.inline_keyboards import (
    main_keyboard, list_course_keyboard, list_teacher_keyboard
)

from locales.message import (
    back_to_main_message_guest, cancel_write_feedback_message, back_to_teachers_message, back_to_courses_list_message, cancel_login_message, not_found_messsage
)


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
    elif request == 'login':
        message = cancel_login_message
        keyboard = main_keyboard()
        state = MainState.main
    else:
        message = not_found_messsage
        keyboard = None
        state = None

    return message, keyboard, state