from locales.keyboard import (
    teacher_panel_keyboard, admin_panel_keyboard, student_panel_keyboard, guest_panel_keyboard
)

from keyboards.main_keyboards import (
    main_keyboards
)

def get_main_keyboard(role):
    if role == 'guest':
        return main_keyboards(guest_panel_keyboard)
    elif role == 'teacher':
        return main_keyboards(teacher_panel_keyboard)
    elif role == 'admin':
        return main_keyboards(admin_panel_keyboard)
    elif role == 'student':
        return main_keyboards(student_panel_keyboard)