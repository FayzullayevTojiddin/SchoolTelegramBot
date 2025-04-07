main_keyboard = {
    "courses" : "🎓 Curslar ro'yxati",
    "teachers" : "👩‍🏫 O'qituvchilar ro'yxati",
    "feedbacks" : "💬 Fikr va takliflar",
    "login" : "🔑 Login"
}

guest_panel_keyboard = {
    "courses" : "🎓 Curslar ro'yxati",
    "teachers" : "👩‍🏫 O'qituvchilar ro'yxati",
    "feedbacks" : "💬 Fikr va takliflar",
    "login" : "🔑 Login"
}


teacher_panel_keyboard = {}

admin_panel_keyboard = {}

student_panel_keyboard = {
    "groups"         : "📚 Guruhlar",
    "notifications"  : "🔔 Bildirishnomalar",
    "profile"        : "👤 Mening Profilim",
    "payments"       : "💸 To'lovlar",
    "quit"           : "🚪 Chiqish"
}

back_main_button_name = {
    'name' : "🔙 Bosh sahifa",
    'callback' : "back:main"
}

cancel_send_feedback_button = {
    'name' : "❌ Bekor qilish",
    'callback' : "back:feedbacks"
}

back_to_course_button = {
    'name' : "🔙 Kurslar",
    'callback' : "back:courses"
}

back_to_teachers_button = {
    'name' : "🔙 O'qituvchilar",
    'callback' : "back:teachers"
}

def back_to_course_btn(course_id):
    return {
        'name' : "🔙 Kursga qaytish",
        'callback' : f"course:{course_id}"
    }

def join_to_course_name(joined, course_id):
    if joined:
        return {
            'name' : "⏳ Yuborildi",
            'callback' : "warning:wait_accepting_join_to_course"
        }
    else:
        return {
            'name' : "📝 Kursga yozilish",
            'callback' : f"join_course:{course_id}"
        }