from aiogram.utils.keyboard import InlineKeyboardBuilder
from locales.keyboard import (
    main_keyboard as main_keyboard_array, 
    back_main_button_name, 
    cancel_send_feedback_button,
    back_to_course_button,
    join_to_course_name,
    back_to_course_btn,
    back_to_teachers_button
)

from models.course import Course
from models.teacher import Teacher
from models.joinCourse import JoinCourse

def main_keyboard():
    keyboard = InlineKeyboardBuilder()
    for callback, name in main_keyboard_array.items():
        keyboard.button(callback_data=callback, text=name)

    keyboard.adjust(2)
    return keyboard.as_markup()

def list_course_keyboard():
    keyboard = InlineKeyboardBuilder()
    for course in Course.select():
        keyboard.button(callback_data=f"course:{str(course.id)}", text=course.name)

    keyboard.button(
        text=back_main_button_name['name'],
        callback_data=back_main_button_name['callback']
    )
    keyboard.adjust(1)
    return keyboard.as_markup()

def list_teacher_keyboard():
    keyboard = InlineKeyboardBuilder()
    teachers = Teacher.select()
    if teachers.exists():
        for teacher in teachers:
            keyboard.button(callback_data=f"teacher:{str(teacher.id)}", text=teacher.full_name)

    keyboard.button(
        text=back_main_button_name['name'],
        callback_data=back_main_button_name['callback']
    )
    keyboard.adjust(1)
    return keyboard.as_markup()

def cancel_feedback_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text=cancel_send_feedback_button['name'],
        callback_data=cancel_send_feedback_button['callback']
    )
    return keyboard.as_markup()

def get_teacher_from_course(teachers, user_id, course_id):
    keyboard = InlineKeyboardBuilder()
    for teacher in teachers:
        keyboard.button(callback_data=f"teacher:{str(teacher.id)}", text=teacher.full_name)    
    joined = JoinCourse.check_join(user_id, course_id)
    button = join_to_course_name(joined, course_id)
    keyboard.button(
        text=button['name'],
        callback_data=button['callback']
    )
    keyboard.button(
        text=back_to_course_button['name'],
        callback_data=back_to_course_button['callback']
    )
    keyboard.adjust(1)
    return keyboard.as_markup()

def back_to_course_keyboard(course_id):
    keyboard = InlineKeyboardBuilder()
    button = back_to_course_btn(course_id)
    keyboard.button(
        text=button['name'],
        callback_data=button['callback']
    )
    return keyboard.as_markup()

def show_teacher_keyboard(teacher_id):
    keyboard = InlineKeyboardBuilder()
    teacher = Teacher.get_by_id(teacher_id)
    courses = Teacher.get_courses(teacher_id)
    for course in courses:
        keyboard.button(
            text=course.name,
            callback_data=f"course:{course.id}"
        )
    button = back_to_teachers_button
    keyboard.button(
        text="📞 Bog‘lanish",
        url=f"https://t.me/{teacher.telegram}"
    )
    keyboard.button(
        text=button['name'],
        callback_data=button['callback']
    )
    keyboard.adjust(1)
    return keyboard.as_markup()