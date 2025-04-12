
from models.notification import Notification

def send_notification(from_in, for_to, message):
    try:
        Notification.create(
            from_in = from_in,
            to = for_to,
            message = message,
            hidden = False,
            read = False
        )
    except Exception as error:
        print(error)
        return False