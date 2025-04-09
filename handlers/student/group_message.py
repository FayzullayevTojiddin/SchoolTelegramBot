from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from services.student.group_services import (
    show_group, get_group
)

from services.student.group_material_services import (
    get_list_materail, get_material
)

from services.any.students_list_services import get_students_list

router = Router(name=__name__)

@router.callback_query(F.data.startswith('group:'))
async def show_group_joined_user(callback: types.CallbackQuery, state: FSMContext):
    group_id = callback.data.split(':')[1]
    response = show_group(1, group_id)
    if response:
        text, keyboard, state = response
        await callback.bot.edit_message_text(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            text=text,
            reply_markup=keyboard
        )
    else:
        await callback.answer("Error")

@router.callback_query(F.data.startswith('group_about:'))
async def get_about_group_message(callback: types.CallbackQuery, state: FSMContext):
    group_id = callback.data.split(':')[1]
    response = get_group(1, group_id)
    if response:
        text, keyboard, state = response
        await callback.bot.send_message(
            chat_id=callback.from_user.id,
            text=text,
            reply_markup=keyboard
        )
    else:
        await callback.answer("Error")

@router.callback_query(F.data.startswith('materials:group_id='))
async def get_materials_message(callback: types.CallbackQuery, state: FSMContext):
    group_id = callback.data.split('materials:group_id=')[1]
    response = get_list_materail(group_id, 1)
    if response:
        text, keyboard, state = response
        await callback.bot.edit_message_text(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            text=text,
            reply_markup=keyboard
        )
    else:
        await callback.answer("Error")

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

@router.callback_query(F.data.startswith('inGroupStudents:group='))
async def get_list_students_message(callback: types.CallbackQuery, state: FSMContext):
    group_id = callback.data.split('inGroupStudents:group=')[1]
    response = get_students_list(group_id, 1)
    if response:
        text, keyboard, state = response
        await callback.bot.edit_message_text(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            text=text,
            reply_markup=keyboard
        )
    else:
        await callback.answer("Error")