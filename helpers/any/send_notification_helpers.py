
from models.notification import Notification

def send_notification(from_in, for_to, message):
    try:
        Notification.create(
            
        )
    except Exception as error:
        print(error)
        return False