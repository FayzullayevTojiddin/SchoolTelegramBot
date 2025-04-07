from models.user import User
from models.login import Login


def get_payments(user_id):
    user = User.get_user(user_id)
    login = user.login
    student = login.student.get()
    return student.payments.select()

def get_payments_message(payments):
    count = len(payments)
    total_price = sum(payment.price for payment in payments)

    return (
        f"💸 Sizda {count} ta to'lov mavjud.\n\n"
        f"Umumiy to'lov summasi: {total_price} so'm"
    )