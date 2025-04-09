from aiogram import Router

from .guest import router as guest_handlers_router
from .student import router as student_handlers_router
from .start_message import router as start_message
from .main_messages import router as main_message
from .back_message import router as back_message

router = Router(name=__name__)

router.include_routers(
    start_message, main_message, back_message, guest_handlers_router, student_handlers_router
)