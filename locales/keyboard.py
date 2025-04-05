main_keyboard = {
    "courses" : "🎓 Curslar ro'yxati",
    "teachers" : "👩‍🏫 O'qituvchilar ro'yxati",
    "feedbacks" : "💬 Fikr va takliflar",
    "login" : "🔑 Login"
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