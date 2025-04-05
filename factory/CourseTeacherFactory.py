from faker import Faker

from models.CourseTeacher import CourseTeacher

import random

faker = Faker()

def create_CourseTeacher(count: int):
    for _ in range(count):
        CourseTeacher.create(
            course_id=random.randint(1, 5),
            teacher_id=random.randint(1, 10)
        )