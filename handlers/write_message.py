from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from services.any.send_message_service import (
    send_message_request_to_response, send_message_to
)

from states.any_states import SendMessage

router = Router(name=__name__)

@router.callback_query(F.data.startswith('write-teacher:'))
@router.callback_query(F.data.startswith('write-message:'))
async def get_message_for_writing(callback: types.CallbackQuery, state: FSMContext):
    try:
        response = await send_message_request_to_response(callback, state)
        text, keyboard, state_to = response
        await callback.bot.send_message(
            chat_id=callback.from_user.id,
            text=text,
            reply_markup=keyboard
        )
        await state.set_state(state_to)
    except Exception as error:
        print(error)
        await callback.answer(
            text="Bot tomonidan no'malumo xatolik"
        )

@router.message(SendMessage.get_message)
async def send_notification_to(message: types.Message, state: FSMContext):
    try:
        text, keyboard, state_to = await send_message_to(message, state)
        await message.answer(
            text=text,
            reply_markup=keyboard,
            reply_to_message_id=message.message_id,
        )
        await state.set_state(state_to)
    except Exception as error:
        print(error)
        await message.answer(
            text="Problem in bot"
        )