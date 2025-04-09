
from helpers.materials_helper import (
    get_materials, get_materials_message, get_material as get_material_helper, get_material_message
)
from helpers.student.get_group_list import check_join_student
from keyboards.index_keyboars import materials_list_keyboard

def get_list_materail(group_id, student_id):
    checkJoin = check_join_student(student_id, group_id)
    if checkJoin:
        materials = get_materials(group_id)
        keyboard = materials_list_keyboard(materials, group_id)
        text = get_materials_message(group_id, len(materials))
        state = None
        return text, keyboard, state
    else:
        return False
    
def get_material(material_id):
    material = get_material_helper(material_id)
    if material:
        keyboard = None
        text = get_material_message(material)
        state = None
        document = material.path
        return text, keyboard, state, document
    else:
        return False