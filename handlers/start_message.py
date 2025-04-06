from aiogram import Router, types
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from states.any_states import MainState
from locales.message import start_message as start_message_text
from keyboards.inline_keyboards import main_keyboard
from helpers.main_state_helper import get_main_keyboard
from models.user import User

router = Router(name=__name__)

@router.message(CommandStart())
async def start_message(message: types.Message, state: FSMContext):
    role = User.get_role(message.from_user.id)
    response = get_main_keyboard(role)
    await message.answer(
        text=start_message_text,
        reply_markup=response
    )
    await state.clear()
    await state.set_state(MainState.main)