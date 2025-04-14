from aiogram.utils.keyboard import InlineKeyboardBuilder


def materials_list_keyboard(materials, group_id):
    keyboard = InlineKeyboardBuilder()
    for material in materials:
        keyboard.button(
            text=material.name,
            callback_data=f"material:{material.id}"
        )
    keyboard.button(
        text="🔙 guruhga qaytish",
        callback_data=f"group:{group_id}"
    )
    keyboard.adjust(1)
    return keyboard.as_markup()

def students_list_keyboard(students, group_id):
    keyboard = InlineKeyboardBuilder()
    for student in students:
        keyboard.button(
            text=student.first_name,
            callback_data=f"student:{student.id}"
        )
    keyboard.button(
        text="🔙 guruhga qaytish",
        callback_data=f"group:{group_id}"
    )
    keyboard.adjust(1)
    return keyboard.as_markup()

def homeWorkListKeyboard(homeworks, group_id):
    keyboard = InlineKeyboardBuilder()
    for homework in homeworks:
        keyboard.button(
            text=homework.title, callback_data=f"homework:{homework.id}=group_id:{group_id}"
        )
    keyboard.button(
        text="🔙 guruhga qaytish",
        callback_data=f"group:{group_id}"
    )
    keyboard.adjust(1)
    return keyboard.as_markup()