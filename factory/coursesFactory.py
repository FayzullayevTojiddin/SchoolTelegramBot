from faker import Faker
from models.course import Course

faker = Faker()

def create_course(count: int):
    try:
        for _ in range(count):
            Course.create(
                name = faker.name(),
                description = faker.text()
            )
    except Exception as error:
        raise Exception(error)