from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from helpers.teacher_helper import get_teacher

from locales.message import not_found_teacher

router = Router(name=__name__)

@router.callback_query(F.data.startswith('teacher:'))
async def get_teacher_message(callback: types.CallbackQuery, state: FSMContext):
    teacher_id = callback.data.split(":")[1]
    response = get_teacher(teacher_id)
    if response:
        message, keyboard = response
        await callback.bot.send_message(
            chat_id=callback.from_user.id,
            text=message,
            reply_markup=keyboard
        )
    else:
        await callback.answer(not_found_teacher, show_alert=True)