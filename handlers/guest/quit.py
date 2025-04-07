from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from helpers.quit_helper import quit_account

from locales.message import not_found_messsage

router = Router(name=__name__)

@router.callback_query(F.data == "quit")
async def quit_is_account(callback: types.CallbackQuery, state: FSMContext):
    response = quit_account(callback.from_user.id)
    if response:
        message, keyboard, state_to = response
        await callback.bot.edit_message_text(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            text=message,
            reply_markup=keyboard
        )
        await state.set_state(state_to)
    else:
        await callback.answer(
            text=not_found_messsage
        )