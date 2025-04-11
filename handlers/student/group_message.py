from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from services.student.group_material_services import get_material

from services.student.get_group_response import get_group_response

from states.student import StudentGroups

router = Router(name=__name__)


@router.callback_query(F.data.startswith('material:'))
async def get_material_message(callback: types.CallbackQuery, state: FSMContext):
    material_id = callback.data.split('material:')[1]
    response = get_material(material_id)
    if response:
        text, keyboard, state, document = response
        await callback.bot.send_document(
            chat_id=callback.from_user.id,
            caption=text,
            reply_markup=keyboard,
            document=document
        )
    else:
        await callback.answer("Error")

@router.callback_query(StudentGroups.main)
async def in_group_handlers_message(callback: types.CallbackQuery, state: FSMContext):
    try:
        response = get_group_response(callback)
        if response:
            text, keyboard, state = response
            await callback.bot.edit_message_text(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                text=text,
                reply_markup=keyboard
            )
        else:
            await callback.answer("Not Found")
    except Exception as error:
        await callback.answer("Xatolik bot tomindan tez orada ko'rib chiqiladi")
        print(error)