
from helpers.any.get_notification_helpers import (
    get_notification as get_notification_helper, get_notification_message
)

from keyboards.about_keyboards import get_about_notification_keyboard

def get_notification(notification_id, student_id):
    notification = get_notification_helper(notification_id)
    if notification and notification.to_id == student_id:
        keyboard = get_about_notification_keyboard()
        text = get_notification_message(notification)
        state = None
        return text, keyboard, state
    else:
        return False