from faker import Faker
from models.group import Group

faker = Faker()

def create_group(count: int):
    for _ in range(count):
        Group.create(
            teacher_id = faker.random_int(min=1, max=10),
            course_id = faker.random_int(min=1, max=5),
            name=faker.name()
        )