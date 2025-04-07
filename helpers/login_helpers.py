from models.login import Login
from models.user import User

from locales.message import (
    isset_login_true, isset_login_false, password_false, password_true
)

from keyboards.cancel_ceyboards import cancel_login_keyboard

from states.any_states import (
    LoginState
)

from .get_role_helper import get_role_state
from .get_main_keyboard_helper import get_main_keyboard

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
            login = Login.isset_login(data['login'])
            role = login.role
            keyboard = get_main_keyboard(role)
            message = password_true
            state_to = get_role_state(role)
            log_to(login.role, user_id, login.id)
            await state.clear()
            await state.set_state(state_to)
        else:
            message = password_false
            keyboard = cancel_login_keyboard()
            await state.set_state(LoginState.password)

        return message, keyboard
    except Exception as error:
        print(error)
        return False

def log_to(role, user_id, login_id):
    user = User.get_user(user_id)
    if user:
        user.role = role
        user.login = login_id
        user.save()