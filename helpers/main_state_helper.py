from services.guest.get_main_response import get_main_response_guest
from services.student.get_main_response import get_main_response_student

def main_state_response(request, role):
    if role == 'guest':
        return get_main_response_guest(request)
    elif role == 'student':
        return get_main_response_student(request)