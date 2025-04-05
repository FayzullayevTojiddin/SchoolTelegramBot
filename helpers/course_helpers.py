from models.course import Course
from keyboards.inline_keyboards import get_teacher_from_course, back_to_course_keyboard
from locales.message import join_request_sended_true
from states.any_states import CourseState
from models.joinCourse import JoinCourse

def show_course(course_id, user_id):
    try:
        course = Course.get_by_id(course_id)
        teachers = Course.get_teachers(course.id)
        message = (
            f"📚 *{course.name}*\n\n"
            f"{course.description}\n\n"
            f"💵 *Narx:* {course.price:,} so'm\n"
            f"⏳ *Davomiyligi:* {course.duration}\n"
        )
        keyboard = get_teacher_from_course(teachers, user_id, course.id)
        state = CourseState.select
        return message, keyboard, state
    except Exception as e:
        print(f"Error: {e}")
        return False

def join_course(course_id, user_id):
    response = JoinCourse.join(user_id, course_id)
    if response:
        message = join_request_sended_true
        keyboard = back_to_course_keyboard(course_id)
        return message, keyboard
    else:
        return False