start_message = """
**Xush kelibsiz!**  
Sizni o'quv markazimizda ko'rishdan xursandmiz! 😊  
Quyidagi tugmalar orqali kerakli xizmatlarga o'tishingiz mumkin:
"""

courses_message = """
Bizning kurslarimizni tanlash orqali ta'limda yangi imkoniyatlar oching!  
Quyida ta'lim dasturlarimiz bilan tanishing. Sizga qulay kursni tanlashda yordam berishga tayyormiz! 🌟  
Agar qo'shimcha ma'lumot olishni xohlasangiz, biz bilan bog'laning! 📚 
"""

teachers_message = """
Bizning malakali o'qituvchilarimiz sizni kutmoqda!  
Ular nafaqat bilim, balki haqiqiy hayotiy tajribalarni ham sizga taqdim etadi.  
Har bir o'qituvchi o'z sohasida yetakchi mutaxassis va sizni har tomonlama qo'llab-quvvatlashga tayyor. 🌟  
Agar o'qituvchilarimiz haqida ko'proq bilmoqchi bo'lsangiz, biz bilan bog'laning! ✨
"""

feedbak_message = """
Sizning fikrlaringiz biz uchun juda muhim!  
Agar kurslarimiz yoki xizmatlarimizga oid taklif yoki fikrlaringiz bo'lsa, iltimos, bizga yuboring.  
Biz har bir fikrni diqqat bilan o'rganib, imkon qadar yaxshilanishga harakat qilamiz.🙏  
Har qanday taklif yoki fikr uchun rahmat! 🌟
"""

login_message = """
Hisobingizga kirish uchun loginni kiiriting.  
Barcha kerakli ma'lumotlar uchun biz bilan bog'laning.  
Hisobingizga kiring va ta'limni boshlang! 📚
"""

not_found_messsage = """
**❌ No'malum buyruq**  
Kechirasiz, siz kiritgan buyruq tanilmagan. Iltimos, to'g'ri buyruqni tanlang yoki yordam uchun quyidagi variantlarni sinab ko'ring.  
"""

back_to_main_message = """
🔙 **Bosh sahifaga qaytdingiz!** ✨
"""

back_to_courses_list_message = """
🔙 **Kurslar ro'yxatiga qaytdingiz!** 📚
"""

back_to_teachers_message = """
🔙 **Ustozlar ro'yxatiga qaytdingiz!** 🧑‍🏫
"""

cancel_write_feedback_message = """
✖️ Fikr bildirish bekor qilindi. Bosh sahifaga qaytdingiz.
"""

cancel_login_message = """
✖️ Loginga kirish bekor qilindi. Bosh sahifaga qaytdingiz.
"""

not_found_course = """
*❌ Kurs topilmadi.*
"""

join_request_sended_true = """
📝 *So'rovingiz yuborildi!*
Iltimos kutib turing, tez orada javob beramiz. 💬
Agar boshqa savollaringiz bo'lsa, bizga yozing! 😊
"""

join_request_sended_false = """
Xabar yuborishda xatolik. 
"""

not_found_teacher = """
*❌ O'qituvchi topilmadi.*
"""

success_sended_feedback = "😊 Fikringiz uchun tashakkur! \n\nBiz uni albatta ko‘rib chiqamiz va xizmatimizni yanada yaxshilashga harakat qilamiz!"

isset_login_true = """
🔐 *Parolingizni kiriting:*
Iltimos, quyidagi maydonga **parolingizni** kiriting.
⚠️ *Eslatma:* Parol maxfiy bo‘lishi kerak va hech kimga ko‘rsatmaslikka harakat qiling.
✋ Agar parolni unutgan bo'lsangiz, yordam uchun admin bilan bog'laning.
"""

isset_login_false = """
❌ *Login noto‘g‘ri kiritildi!*
Iltimos, **to‘g‘ri loginni** qayta kiriting.

⚠️ Agar login unutgan bo‘lsangiz, yordam uchun admin bilan bog'laning.
"""

write_message_please_message = """
🙅‍♂️ Xato! Faqat matn kiriting, boshqa turdagi fayl yubormang!
"""

password_true = """
✅ Tizimga muvaffaqiyatli kirish amalga oshirildi!
"""

password_false = """
❌ *Parol noto‘g‘ri kiritildi!*
Iltimos, **to‘g‘ri parolni** qayta kiriting.

⚠️ Agar parolni unutgan bo‘lsangiz, yordam uchun admin bilan bog'laning.
"""

quit_message = """
🚪 Chiqdingiz.
"""

list_groups_message_student = """
📚 *Siz a'zo bo‘lgan guruhlar:*
 """

this_student_you = "O'zingizga xabar yubora olmaysiz !"

get_message_to_send = """
📨 Xabar yuborish

Quyida yozmoqchi bo‘lgan xabaringiz matnini kiriting.
Ushbu xabar to‘g‘ridan-to‘g‘ri o‘quvchiga yuboriladi.

✍️ Yozishni boshlashingiz mumkin.
"""

get_message_canel_to_send = """
✖️ Xabar yuborish bekor qilindi. Bosh sahifaga qaytdingiz.
"""

message_is_not_text_error = """
🤖 Xatolik: Bu yerda faqat matnli xabar yuborishingiz mumkin.
Iltimos, boshqa turdagi kontent yubormang.
"""

message_sent_successfully = "✅ Sizning xabaringiz muvaffaqiyatli tarzda yuborildi."

notification_deleted_successfully = "✅ Xabar muvaffaqiyatli o‘chirildi."

notification_deleted_error = "❗️ Xabarni o‘chirib bo‘lmadi, qayta urinib ko‘ring."

def get_student_message(student):
    return (
        "👤 *O‘quvchi ma’lumotlari*\n\n"
        f"📛 *Ismi:* {student.first_name} {student.last_name}\n"
        f"🧔 *Otasining ismi:* {student.father_name}\n"
        f"🎂 *Tug‘ilgan sanasi:* {student.birthday}\n"
        f"📝 *Qo‘shimcha ma’lumot:* {student.description or '–'}\n"
        f"📅 *Ro‘yxatga olingan sana:* {student.created_at.strftime('%Y-%m-%d')}\n"
        f"📌 *Holati:* {'Faol ✅' if student.status else 'Faol emas ❌'}"
    )