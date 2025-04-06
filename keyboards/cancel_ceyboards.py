from aiogram.utils.keyboard import InlineKeyboardBuilder

def cancel_login_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="❌ Bekor qilish",
        callback_data='back:login'
    )
    return keyboard.as_markup()