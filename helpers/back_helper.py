from aiogram import Bot, types

from models.user import User

from services.guest.back_services import get_request_from_guest

from services.student.back_services import get_request_from_student
    
def get_back_response(callback: types.CallbackQuery):
    role = User.get_role(callback.from_user.id)
    try:
        return responses_from_role(role, callback)
    except:
        return False

def responses_from_role(role, callback):
    if role == 'guest':
        return get_request_from_guest(callback)
    elif role == 'student':
        return get_request_from_student(callback)
    elif role == 'teacher':
        pass
    elif role == 'admin':
        pass
    else:
        return False