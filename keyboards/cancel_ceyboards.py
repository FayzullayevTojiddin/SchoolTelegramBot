from aiogram.utils.keyboard import InlineKeyboardBuilder

def cancel_login_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="❌ Bekor qilish",
        callback_data='back:login'
    )
    return keyboard.as_markup()

def cancel_message_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="❌ Bekor qilish",
        callback_data='back:message'
    )
    return keyboard.as_markup()

def back_to_notifications_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="🔙 Bildirishnomalarga qaytish",
        callback_data="notifications"
    )
    return keyboard.as_markup()