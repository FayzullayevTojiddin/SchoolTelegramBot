from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from services.any.send_message_service import send_message_request_to_response

from states.any_states import SendMessage

router = Router(name=__name__)

@router.callback_query(F.data.startswith('write-message:'))
async def get_message_for_writing(callback: types.CallbackQuery, state: FSMContext):
    try:
        old_state = await state.get_state()
        response = send_message_request_to_response(callback, old_state)
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
    pass