from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from services.any.students_list_services import select_student_message

router = Router(name=__name__)

@router.callback_query(F.data.startswith('student:'))
async def get_student_message(callback: types.CallbackQuery, state: FSMContext):
    try:
        text, keyboard, state_to = select_student_message(callback)
        await callback.bot.send_message(
            chat_id=callback.from_user.id,
            text=text,
            reply_markup=keyboard
        )
    except Exception as error:
        print(error)
        await callback.answer(
            text="Botda nosozlik"
        )