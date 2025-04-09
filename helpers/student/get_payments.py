from models.user import User
from models.paymentStudent import PaymentStudent



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

def get_payment(payment_id):
    return PaymentStudent.get_by_id(payment_id)

def get_payment_message(payment):
    return (
        f"🧾 *To‘lov ma'lumotlari*\n"
        f"👤 Student ID: `{payment.login.id}`\n"
        f"💰 Narxi: *{payment.price} so'm*\n"
        f"📝 Izoh: {payment.description or '—'}\n"
        f"📅 Sana: {payment.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    )