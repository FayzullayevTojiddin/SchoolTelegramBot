from aiogram.utils.keyboard import InlineKeyboardBuilder

from locales.keyboard import (
    back_main_button_name, show_group_student_button
)
def get_groups_keyboard(groups):
    keyboard = InlineKeyboardBuilder()
    for group in groups:
        keyboard.button(text=f"📚 {group.name}", callback_data=f"group:{group.id}")

    keyboard.button(
        text=back_main_button_name['name'],
        callback_data=back_main_button_name['callback']
    )
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_my_profile_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text=back_main_button_name['name'],
        callback_data=back_main_button_name['callback']
    )
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_notifications_keyboard(notifications):
    keyboard = InlineKeyboardBuilder()
    for notification in notifications:
        keyboard.button(
            text=f"🔔: {notification.id}",
            callback_data=f"notification:{notification.id}"
        )
    keyboard.button(
        text=back_main_button_name['name'],
        callback_data=back_main_button_name['callback']
    )
    keyboard.adjust(1)
    return keyboard.as_markup()

def get_payments_keyboard(payments):
    keyboard = InlineKeyboardBuilder()
    for payment in payments:
        keyboard.button(
            text=f"💸 : {payment.price}",
            callback_data=f"payment:{payment.id}"
        )
    keyboard.button(
        text=back_main_button_name['name'],
        callback_data=back_main_button_name['callback']
    )
    keyboard.adjust(1)
    return keyboard.as_markup()

def show_group_keyboard(group_id, teacher_id):
    keyboard = InlineKeyboardBuilder()
    buttons = show_group_student_button(group_id, teacher_id)
    for callback, name in buttons.items():
        keyboard.button(text=name, callback_data=callback)
    keyboard.button(
        text="🔙 Kurslar ro'yxatiga qaytish",
        callback_data="back:groups"
    )
    keyboard.adjust(1)
    return keyboard.as_markup()
