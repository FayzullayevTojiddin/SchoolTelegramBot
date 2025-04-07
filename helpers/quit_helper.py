from models.user import User

from keyboards.inline_keyboards import main_keyboard

from locales.message import quit_message

from states.any_states import MainState

def quit_account(user_id):
    user = User.get_user(user_id)
    if user:
        user.role = 'guest'
        user.login = None
        user.save()
        keyboard = main_keyboard()
        message = quit_message
        state = MainState.main
        return message, keyboard, state
    else:
        return False