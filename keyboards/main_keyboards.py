from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_keyboards(keyboards_array):
    keyboard = InlineKeyboardBuilder()
    for callback, name in keyboards_array.items():
        keyboard.button(callback_data=callback, text=name)

    keyboard.adjust(1)
    return keyboard.as_markup()