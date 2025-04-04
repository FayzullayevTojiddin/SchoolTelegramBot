from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from models.course import Course

router = Router(name=__name__)


@router.callback_query(F.data.startswith('course:'))
async def select_course_message(callback: types.CallbackQuery, state: FSMContext):
    course_id = callback.data.split(":")[1]
    course = Course.get_by_id(course_id)