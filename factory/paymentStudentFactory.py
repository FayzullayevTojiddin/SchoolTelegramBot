from faker import Faker
import random

faker = Faker()

from models.paymentStudent import PaymentStudent

def create_studentPayment(count: int):
    for _ in range(count):
        PaymentStudent.create(
            login = 1,
            price = random.randint(500, 2000) * 1000,
            description = faker.text()
        )