from aiogram.utils.keyboard import ReplyKeyboardBuilder

def getCancelKeyboard():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Ro'yxatdan o'tish")
    keyboard.adjust(1)
    return keyboard.as_markup(resize_keyboard=True)