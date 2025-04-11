
from helpers.any.get_notification_helpers import (
    get_notification as get_notification_helper, get_notification_message, delete_notification_helper
)

from helpers.student.get_student import (
    get_student_id, get_student
)

from locales.message import (
    notification_deleted_successfully, notification_deleted_error
)

from helpers.any.get_login import get_login_by_student_id

from keyboards.about_keyboards import get_about_notification_keyboard
from keyboards.cancel_ceyboards import back_to_notifications_keyboard

from states.student import StudentMain

def get_notification(notification_id, user_id):
    student_id = get_student_id(user_id)
    login = get_student(student_id).login
    notification = get_notification_helper(notification_id)
    if notification and notification.to_id == login.id:
        keyboard = get_about_notification_keyboard(notification_id)
        text = get_notification_message(notification)
        state = StudentMain.main
        return text, keyboard, state
    else:
        return False
    
def delete_notification(callback, old_state):
    notification_id = callback.data.split(":")[1]
    notification = get_notification_helper(notification_id)
    student_id = get_student_id(callback.from_user.id)
    login_id = get_login_by_student_id(student_id)
    if notification and notification.from_in_id == login_id and delete_notification_helper(notification_id):
        keyboard = back_to_notifications_keyboard()
        text = notification_deleted_successfully
        state = old_state
    else:
        text, keyboard, state = get_notification(notification_id, callback.from_user.id)
        text = notification_deleted_error

    return text, keyboard, state