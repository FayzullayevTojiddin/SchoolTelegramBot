from aiogram import Bot

from models.user import User

from services.back_services import get_request_from_guest

def get_back_response(bot: Bot, request, user_id: int):
    role = User.get_role(user_id)
    try:
        return responses_from_role(role, request)
    except:
        return False

def responses_from_role(role, request):
    if role == 'guest':
        return get_request_from_guest(request)
    elif role == 'teacher':
        pass
    elif role == 'admin':
        pass
    else:
        return False