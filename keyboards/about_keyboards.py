from aiogram.utils.keyboard import InlineKeyboardBuilder
from locales.keyboard import back_main_button_name

def back_to_group_keyboard(group_id):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="🔙 guruhga qaytish",
        callback_data=f"group:{group_id}"
    )
    return keyboard.as_markup()

def get_about_payment_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="🔙 To'lovlarga qaytish",
        callback_data="payments"
    )
    return keyboard.as_markup()

def get_about_notification_keyboard(notification_id):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="🗑️ Xabarni o‘chirish",
        callback_data=f"delete_notification:{notification_id}"
    )
    keyboard.button(
        text="🔙 Bildirishnomalarga qaytish",
        callback_data="notifications"
    )
    keyboard.adjust(1)
    return keyboard.as_markup()