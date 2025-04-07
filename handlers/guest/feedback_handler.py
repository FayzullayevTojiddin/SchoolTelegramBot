from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from locales.message import success_sended_feedback

from keyboards.inline_keyboards import main_keyboard, cancel_feedback_keyboard

from states.any_states import MainState

from states.any_states import FeedbakState

from helpers.feedback_helper import get_request

router = Router(name=__name__)

@router.message(FeedbakState.main)
async def get_feedback_message(message: types.Message, state: FSMContext):
    response = get_request(message.text, message.from_user.id)
    if response:
        await message.answer(
            text=success_sended_feedback,
            reply_markup=main_keyboard()
        )
        await state.set_state(MainState.main)
    else:
        await message.answer(
            text="⚠️ Afsuski, hozircha fikringizni yuborib bo‘lmadi.\nIltimos, keyinroq yana urinib ko‘ring. Texnik nosozlik bo‘lishi mumkin.",
            reply_markup=cancel_feedback_keyboard()
        )