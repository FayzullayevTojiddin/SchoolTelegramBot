
from keyboards.student_keyboards import get_groups_keyboard

from helpers.student import get_groups

def get_main_response_student(request, user_id):
    if request == 'groups':
        groups = get_groups(user_id)
        keyboard = get_groups_keyboard(groups)
        text = ...
        state = ...
    
    return keyboard, text, state