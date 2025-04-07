from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from helpers.course_helpers import show_course, join_course
from locales.message import (
    not_found_course,
    join_request_sended_false
)

router = Router(name=__name__)


@router.callback_query(F.data.startswith('course:'))
async def select_course_message(callback: types.CallbackQuery, state: FSMContext):
    course_id = callback.data.split(":")[1]
    response = show_course(course_id, callback.from_user.id)
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
        await callback.answer(text=not_found_course, show_alert=True)

@router.callback_query(F.data.startswith('join_course:'))
async def join_to_course_message(callback: types.CallbackQuery, state: FSMContext):
    course_id = callback.data.split(":")[1]
    response = join_course(course_id, callback.from_user.id)
    if response:
        message, keyboard = response
        await callback.bot.edit_message_text(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            text=message,
            reply_markup=keyboard
        )
    else:
        await callback.answer(text=join_request_sended_false, show_alert=True)