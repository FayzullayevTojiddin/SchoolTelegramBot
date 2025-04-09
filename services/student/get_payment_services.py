
from helpers.student.get_payments import (
    get_payment as get_payment_helper, get_payment_message
)

from keyboards.about_keyboards import get_about_payment_keyboard

def get_payment(student_id, payment_id):
    payment = get_payment_helper(payment_id)
    if payment and payment.login_id == student_id:
        keyboard = get_about_payment_keyboard()
        text = get_payment_message(payment)
        state = None
        return text, keyboard, state
    else:
        return False