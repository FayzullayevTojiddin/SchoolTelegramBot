
from helpers.student.get_payments import (
    get_payment as get_payment_helper, get_payment_message
)

from helpers.student.get_student import get_student_id

from keyboards.about_keyboards import get_about_payment_keyboard

from states.student import StudentMain

def get_payment(user_id, payment_id):
    student_id = get_student_id(user_id)
    payment = get_payment_helper(payment_id)
    if payment and payment.login_id == student_id:
        keyboard = get_about_payment_keyboard()
        text = get_payment_message(payment)
        state = StudentMain.main
        return text, keyboard, state
    else:
        return False