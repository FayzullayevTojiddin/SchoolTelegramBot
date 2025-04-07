from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from helpers.main_state_helper import main_state_response

from states.student import StudentMain

from models.user import User

from helpers.not_found import not_found_message

router = Router(name=__name__)

@router.callback_query()
async def main_state_message(callback: types.CallbackQuery, state: FSMContext):
    role = User.get_role(callback.from_user.id)
    response = main_state_response(callback.data, role, callback.from_user.id)
    if response:
        keyboard, text, state_to = response
        await callback.bot.edit_message_text(
            text=text,
            reply_markup=keyboard,
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
        )
        await state.set_state(state_to)
    else:
        await not_found_message(callback.bot, callback.from_user.id)