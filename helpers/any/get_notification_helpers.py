
from models.notification import Notification

from helpers.any.get_login import get_first_name

def get_notification(notification_id):
    return Notification.get_by_id(notification_id)

def get_notification_message(notification: Notification) -> str:
    status = "📬 Yangi xabar" if not notification.read else "✅ Ilgari o‘qilgan"
    first_name = get_first_name(notification.from_in_id)
    return (
        f"{status}\n"
        f"👤 Kimdan: {first_name}\n"
        f"🕒 Sana: {notification.created_at.strftime('%Y-%m-%d %H:%M')}\n\n"
        f"💬 Xabar:\n{notification.message}"
    )

def delete_notification_helper(notification_id):
    try:
        notification = Notification.get_by_id(notification_id)
        notification.hidden = True
        notification.save()
        return True
    except Exception as error:
        print(error)
        return False