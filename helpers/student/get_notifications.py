from models.user import User
from models.notification import Notification

from .get_student import (
    get_student_id, get_student
)

def get_notifications(user_id):
    student_id = get_student_id(user_id)
    student_login = get_student(student_id).login
    return Notification.select().where(Notification.to == student_login, Notification.hidden == False)

def get_notifications_messgae(notifications):
    count = len(notifications)
    return (
        f"📩 Sizda {count} ta o'qilmagan xabar mavjud!\n\nQuyidagi tugmalardan birini tanlang:"
    )