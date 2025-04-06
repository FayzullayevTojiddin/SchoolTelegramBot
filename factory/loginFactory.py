
from models.login import Login

def create_logins():
    Login.create(
        login="admin", password="root", role='admin'
    )

    Login.create(
        login="teacher", password="root", role='teacher'
    )

    Login.create(
        login="student", password="root", role='student'
    )

    return True