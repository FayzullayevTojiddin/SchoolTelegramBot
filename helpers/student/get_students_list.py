
from models.GroupStudent import GroupStudent
from models.student import Student

def get_students_list(group):
    return Student.select().join(GroupStudent).where(GroupStudent.group == group)

def get_students_message(group_id, students_count):
    return (
        f"📚 *Guruhdagi o'quvchilar*\n\n"
        f"🆔 *Guruh ID:* {group_id}\n"
        f"👥 *O‘quvchilar soni:* {students_count} ta\n\n"
        f"👇 Quyidagi tugmalar orqali guruh o'quvchilari haqida batafsil ma'lumot olishingiz mumkin."
    )

def get_student_message(student):
    return (
        f"👤 *Ismi:* {student.first_name} {student.last_name}\n"
        f"🧑‍💼 *Otasi ismi:* {student.father_name}\n"
        f"📅 *Tug'ilgan sana:* {student.birthday}\n"
        f"📝 *Izoh:* {student.description if student.description else 'Yo‘q'}\n"
        f"💻 *Status:* {'Faol' if student.status else 'Faol emas'}"
    )