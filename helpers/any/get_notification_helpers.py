
from models.notification import Notification

def get_notification(notification_id):
    return Notification.get_by_id(notification_id)

def get_notification_message(notification: Notification) -> str:
    status = "📬 Yangi xabar" if not notification.readed else "✅ O‘qilgan"
    return (
        f"{status}\n"
        f"👤 Kimdan: IT School\n" ## Sozlash lozim
        f"🕒 Sana: {notification.created_at.strftime('%Y-%m-%d %H:%M')}\n\n"
        f"💬 Xabar:\n{notification.message}"
    )