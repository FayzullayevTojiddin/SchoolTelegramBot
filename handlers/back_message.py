from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from helpers.back_helper import get_back_response
from helpers.not_found import not_found_message

router = Router(name=__name__)

@router.callback_query(F.data.startswith('back:'))
async def back_message(callback: types.CallbackQuery, state: FSMContext):
    action = action = callback.data.split(":")[1]
    response = get_back_response(callback)    
    if response:
        message, keyboard, state_to = response
        await callback.bot.edit_message_text(
            text=message,
            reply_markup=keyboard,
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id
        )
        await state.set_state(state_to)
    else:
        await not_found_message(callback.bot, callback.from_user.id)