

def getHomeWorkListTextHelper(homeworks_count, group_id):
    return (
        f"""📚 Uyga vazifalar

🆔 Guruh ID: {group_id}
📄 Uyga vazifalar soni: {homeworks_count} ta

👇 Quyidagi menyudan kerakli uyga vazifani tanlang:"""
    )

def getHomeWorkDetailTextHelper(homework):
    created_at = homework.created_at.strftime("%d.%m.%Y %H:%M")

    return (
        f"""📌 *Uyga vazifa*
🆔 ID: `{homework.id}`
👥 Guruh: *{homework.group_id.name}*
📅 Yaratilgan sana: _{created_at}_

*📖 {homework.title}*

{homework.description or "ℹ️ Tavsif berilmagan."}"""
    )