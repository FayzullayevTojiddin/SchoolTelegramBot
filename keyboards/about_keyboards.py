from aiogram.utils.keyboard import InlineKeyboardBuilder
from locales.keyboard import back_main_button_name

def get_about_group_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text=back_main_button_name['name'],
        callback_data=back_main_button_name['callback']
    )
    return keyboard.as_markup()

def get_about_payment_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="🔙 To'lovlarga qaytish",
        callback_data="payments"
    )
    return keyboard.as_markup()

def get_about_notification_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="🔙 Bildirishnomalarga qaytish",
        callback_data="notifications"
    )
    return keyboard.as_markup()