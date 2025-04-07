
from models.user import User

def get_student_profile(user_id):
    user = User.get_user(user_id)
    return user.login.student.get()

def get_student_profile_message(my):
    return (
        f"*👤 Mening profilim:*\n\n"
        f"*Ism:* {my.first_name}\n"
        f"*Familiya:* {my.last_name}\n"
        f"*Otasining ismi:* {my.father_name}\n"
        f"*Tug‘ilgan sana:* {my.birthday.strftime('%Y-%m-%d')}\n"
        f"*Holat:* {'✅ Faol' if my.status else '⛔️ Nofaol'}\n"
        f"*Qo‘shimcha ma’lumot:* {my.description if my.description else '—'}\n"
    )