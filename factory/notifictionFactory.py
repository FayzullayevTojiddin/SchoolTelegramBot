from faker import Faker

faker = Faker()

from models.notification import Notification

def create_notification(count: int):
    for _ in range(count):
        Notification.create(
            to = 1,
            from_in = 3,
            message = faker.text(),
            hidden = faker.boolean(),
            readed = faker.boolean()
        )