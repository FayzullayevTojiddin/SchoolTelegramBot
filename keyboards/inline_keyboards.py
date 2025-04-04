from aiogram.utils.keyboard import InlineKeyboardBuilder
from locales.keyboard import main_keyboard as main_keyboard_array, back_main_button_name, cancel_send_feedback_button
from models.course import Course
from models.teacher import Teacher

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