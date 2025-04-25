from aiogram import Router, types
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from locales.message import start_message as start_message_text
from helpers.get_main_keyboard_helper import get_main_keyboard
from models.user import User

from states.any_states import MainState
from states.register import RegisterState

from services.any.register_service import RegisterService

router = Router(name=__name__)


@router.message(CommandStart())
@router.message(RegisterState.main)
@router.message(RegisterState.getFullName)
@router.message(RegisterState.getAge)
@router.message(RegisterState.getPhoneNumber)
async def start_message(message: types.Message, state: FSMContext):
    user = User.get_user(message.from_user.id)
    if user.is_register:
        role = user.role
        response = get_main_keyboard(role)
        await message.answer(
            text=start_message_text,
            reply_markup=response
        )
        await state.set_state(MainState.main)
    else:
        service = RegisterService()
        response = await service.controller(message=message, state=state)
        text, keyboard, newState = response
        await message.answer(
            text=text,
            reply_markup=keyboard
        )
        await state.set_state(newState)