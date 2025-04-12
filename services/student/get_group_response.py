
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
    student_id = get_student_id(callback.from_user.id)
    if action == 'group':
        response = show_group(student_id, value)
    elif action == 'group_about':
        response = get_group(student_id, value)
    elif action == 'materials':
        group_id = callback.data.split('materials:group_id=')[1]
        response = get_list_materail(group_id, student_id)
    elif action == 'inGroupStudents':
        group_id = callback.data.split('inGroupStudents:group=')[1]
        response = get_students_list(group_id, student_id)
    elif action == 'homeworks':
        group_id = callback.data.split('homeworks:group_id=')[1]
        
    else:
        print(callback.data)
        return False

    return response