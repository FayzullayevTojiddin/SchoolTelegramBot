from aiogram import Router

from .guest import router as guest_handlers_router
from .student import router as student_handlers_router

router = Router(name=__name__)

router.include_routers(
    guest_handlers_router, student_handlers_router
)