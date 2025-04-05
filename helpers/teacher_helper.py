from models.teacher import Teacher

from keyboards.inline_keyboards import show_teacher_keyboard

def get_teacher(teacher_id):
    try:
        teacher = Teacher.get_by_id(teacher_id)
        keyboard = show_teacher_keyboard(teacher_id)
        message = (
            f"🧑‍🏫 *{teacher.full_name}*\n\n"
            f"📚 *Mutaxassisligi:* {teacher.subject}\n"
            f"🎓 *Tajriba:* {teacher.experience}\n"
            f"🏫 *Ish joyi:* “{teacher.school}”\n"
            "🏆 *Yutuqlari:*\n"
            f"{teacher.achievements}\n\n"
            f"🗣 *O‘quvchilarning fikri:* “{teacher.feedback}”\n\n"
            "Quyidagi tugmalar orqali bog‘laning yoki darslar bilan tanishing 👇"
        )
        return message, keyboard
    except Exception as error:
        return False