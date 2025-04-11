from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from services.student.get_payment_services import get_payment

router = Router(name=__name__)

@router.callback_query(F.data.startswith('payment:'))
async def get_payment_message(callback: types.CallbackQuery, state: FSMContext):
    payment_id = callback.data.split('payment:')[1]
    response = get_payment(callback.from_user.id, payment_id)
    if response:
        text, keyboard, state_to = response
        await callback.bot.edit_message_text(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            text=text,
            reply_markup=keyboard
        )
        await state.set_state(state_to)
    else:
        await callback.answer(text="Error")