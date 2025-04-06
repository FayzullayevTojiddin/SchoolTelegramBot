from models.login import Login
from models.user import User

from locales.message import (
    isset_login_true, isset_login_false, password_false, password_true
)

from keyboards.cancel_ceyboards import cancel_login_keyboard

from keyboards.inline_keyboards import main_keyboard

from states.any_states import (
    LoginState, MainState
)

async def get_login(login, state):
    try:
        if Login.isset_login(login):
            await state.update_data(login=login)
            message = isset_login_true
            keyboard = cancel_login_keyboard()
            state_to = LoginState.password
        else:
            message = isset_login_false
            keyboard = cancel_login_keyboard()
            state_to = LoginState.login

        return message, keyboard, state_to
    except Exception as error:
        print(error)
        return False
    
async def check_password(password, state, user_id):
    try:
        data = await state.get_data()
        if Login.check_password(data['login'], password):
            await state.clear()
            message = password_true
            keyboard = main_keyboard()
            state_to = MainState.main
            login = Login.isset_login(data['login'])
            log_to(login.role, user_id)
        else:
            message = password_false
            keyboard = cancel_login_keyboard()
            state_to = LoginState.password

        return message, keyboard, state_to
    except Exception as error:
        print(error)
        return False

def log_to(role, user_id):
    user = User.get_user(user_id)
    if user:
        user.role = role
        user.save()