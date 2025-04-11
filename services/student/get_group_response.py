
from aiogram import types


from .group_services import (
    show_group, get_group
)

from .group_material_services import (
    get_list_materail
)

from helpers.student.get_student import get_student_id

from services.any.students_list_services import get_students_list

def get_group_response(callback: types.CallbackQuery):
    value = callback.data.split(":")[1]
    action = callback.data.split(":")[0]
    if action == 'group':
        response = show_group(1, value)
    elif action == 'group_about':
        response = get_group(1, value)
    elif action == 'materials':
        group_id = callback.data.split('materials:group_id=')[1]
        student_id = get_student_id(callback.from_user.id)
        response = get_list_materail(group_id, student_id)
    elif action == 'inGroupStudents':
        group_id = callback.data.split('inGroupStudents:group=')[1]
        student_id = get_student_id(callback.from_user.id)
        response = get_students_list(group_id, student_id)
    else:
        print(callback.data)
        return False

    return response