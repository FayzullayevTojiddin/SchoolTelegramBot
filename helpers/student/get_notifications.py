from models.user import User
from models.notification import Notification

def get_notifications(user_id):
    user = User.get_user(user_id)
    return Notification.select().where(Notification.to == user, Notification.hidden == False)

def get_notifications_messgae(notifications):
    count = len(notifications)
    return (
        f"📩 Sizda {count} ta o'qilmagan xabar mavjud!\n\nQuyidagi tugmalardan birini tanlang:"
    )