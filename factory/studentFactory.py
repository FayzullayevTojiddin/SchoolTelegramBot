from faker import Faker
from models.student import Student

faker = Faker()

def create_student(count: int):
    Student.create(
        id=1,
        first_name="Tojiddin",
        last_name="Fayzullaev",
        father_name="Muhibullo o'g'li",
        description="Intiluvchan talaba",
        birthday='2025-04-08',
        status=True,
        login_id=3
    )
    for _ in range(count):
        Student.create(
            first_name = faker.name(),
            last_name = faker.name(),
            father_name = faker.name(),
            description = faker.text(),
            status = faker.boolean()
        )