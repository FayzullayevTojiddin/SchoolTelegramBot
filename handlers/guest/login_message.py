from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from states.any_states import LoginState

from locales.message import (
    not_found_messsage,
    write_message_please_message
)

from helpers.login_helpers import (
    get_login, check_password
)

router = Router(name=__name__)

@router.message(LoginState.login)
async def get_login_message(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer(text=write_message_please_message)
    else:
        login = message.text
        response = await get_login(login, state)
        if response:
            text, keyboard, state_to = response
            await message.answer(
                text=text,
                reply_markup=keyboard
            )
            await state.set_state(state_to)
        else:
            await message.answer(text=not_found_messsage)

@router.message(LoginState.password)
async def get_password_message(message: types.Message, state: FSMContext):
    if not message.text:
        await message.answer(text=write_message_please_message)
    else:
        password = message.text
        response = await check_password(password, state, message.from_user.id)
        if response:
            text, keyboard = response
            await message.answer(
                text=text,
                reply_markup=keyboard,
            )
        else:
            await message.answer(text=not_found_messsage)