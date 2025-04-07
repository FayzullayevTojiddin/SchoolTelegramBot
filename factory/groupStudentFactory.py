from faker import Faker
from models.GroupStudent import GroupStudent

faker = Faker()

def create_groupStudent(count: int):
    for _ in range(count):
        GroupStudent.create(
            student = 1,
            group = faker.random_int(min=1, max=10)
        )