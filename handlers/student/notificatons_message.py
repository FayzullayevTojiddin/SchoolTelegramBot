from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from services.any.notification_services import get_notification

router = Router(name=__name__)

@router.callback_query(F.data.startswith('notification:'))
async def get_notification_message(callback: types.CallbackQuery, state: FSMContext):
    notification_id = callback.data.split('notification:')[1]
    response = get_notification(notification_id, 1)
    if response:
        text, keyboard, state = response
        await callback.bot.edit_message_text(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            text=text,
            reply_markup=keyboard
        )
    else:
        await callback.answer(text="Error")