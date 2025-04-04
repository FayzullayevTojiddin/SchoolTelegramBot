from aiogram import Router
from .start_message import router as start_message_router
from .main_messages import router as main_message_router
from .back_message import router as back_message_router

router = Router(name=__name__)

router.include_routers(
    start_message_router, main_message_router, back_message_router
)