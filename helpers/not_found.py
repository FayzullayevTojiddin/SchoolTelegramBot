from aiogram import Bot
from locales.message import not_found_messsage

async def not_found_message(bot: Bot, chat_id: int):
    await bot.send_message(
        chat_id=chat_id,
        text=not_found_messsage
    )