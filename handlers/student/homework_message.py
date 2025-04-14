from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from services.student.get_homework_response import get_homework

router = Router(name=__name__)

@router.callback_query(F.data.startswith("homework:"))
async def get_homework_message(callback: types.CallbackQuery, state:FSMContext):
    try:
        homework = callback.data.split("=")[0]
        group = callback.data.split("=")[1]
        homework_id = homework.split(":")[1]
        group_id = group.split(":")[1]
        response = get_homework(homework_id, group_id)
        text, keyboard, state = response
        await callback.bot.edit_message_text(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            text=text,
            reply_markup=keyboard
        )
    except Exception as error:
        print(error)
        await callback.answer(text="Error")