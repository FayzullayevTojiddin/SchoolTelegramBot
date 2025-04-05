from faker import Faker
from models.course import Course
import random

faker = Faker()

def create_course(count: int):
    try:
        for _ in range(count):
            months = random.randint(1, 12)
            days = random.randint(1, 30)
            price = random.randint(500, 2000) * 1000
            teacher = random.randint(1, 5)
            Course.create(
                name = faker.name(),
                description = faker.text(),
                duration = f"{months} oy {days} kun",
                price = price,
                teacher = teacher
            )
    except Exception as error:
        raise Exception(error)