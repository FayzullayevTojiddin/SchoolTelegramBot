from faker import Faker
from models.teacher import Teacher

faker = Faker()

def create_teacher(count: int):
    try:
        for _ in range(count):
            Teacher.create(
                user_id=faker.random_int(min=100000000, max=999999999),
                phone_number=faker.phone_number(),
                full_name=faker.name(),
                description=faker.text()
            )
    except Exception as error:
        raise Exception(error)