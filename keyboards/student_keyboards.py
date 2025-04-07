from aiogram.utils.keyboard import InlineKeyboardBuilder

from locales.keyboard import back_main_button_name

def get_groups_keyboard(groups):
    keyboard = InlineKeyboardBuilder()
    for group in groups:
        keyboard.button(text=group.name, callback_data=f"group:{group.id}")

    keyboard.button(
        text=back_main_button_name['name'],
        callback_data=back_main_button_name['callback']
    )
    keyboard.adjust(1)
    return keyboard.as_markup()