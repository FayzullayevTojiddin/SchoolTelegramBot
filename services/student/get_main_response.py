
from keyboards.student_keyboards import (
    get_groups_keyboard, get_my_profile_keyboard, get_notifications_keyboard, get_payments_keyboard
)

from helpers.student.get_group_list import get_groups
from helpers.student.get_notifications import (
    get_notifications, get_notifications_messgae
)
from helpers.student.get_my_profile import (
    get_student_profile, get_student_profile_message
)
from helpers.student.get_payments import (
    get_payments, get_payments_message
)

from locales.message import list_groups_message_student

from states.student import (
    StudentGroups, StudentMain, NotificationState, StudentPaymenState
)

def get_main_response_student(request, user_id):
    if request == 'groups':
        groups = get_groups(user_id)
        keyboard = get_groups_keyboard(groups)
        text = list_groups_message_student
        state = StudentGroups.main
    elif request == 'profile':
        my = get_student_profile(user_id)
        keyboard = get_my_profile_keyboard()
        text = get_student_profile_message(my)
        state = StudentMain.main
    elif request == 'notifications':
        notifications = get_notifications(user_id)
        keyboard = get_notifications_keyboard(notifications)
        text = get_notifications_messgae(notifications)
        state = NotificationState.main
    elif request == 'payments':
        payments = get_payments(user_id)
        keyboard = get_payments_keyboard(payments)
        text = get_payments_message(payments)
        state = StudentPaymenState.main
            
    return keyboard, text, state