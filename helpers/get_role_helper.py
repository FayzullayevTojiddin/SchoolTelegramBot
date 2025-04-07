
from states.student import StudentMain
from states.guest import GuestMain

def get_role_state(role):
    if role == 'guest':
        return GuestMain.main
    elif role == 'student':
        return StudentMain.main