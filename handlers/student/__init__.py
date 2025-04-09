from aiogram import Router
from .group_message import router as group_message_router
from .payments_message import router as payment_message_router
from .notificatons_message import router as notification_message_router

router = Router(name=__name__)

router.include_routers(
    group_message_router,
    payment_message_router,
    notification_message_router
)