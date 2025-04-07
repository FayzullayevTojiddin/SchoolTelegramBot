from aiogram import Router

from .main_message import router as main_message_router

router = Router(name=__name__)

router.include_routers(
    main_message_router
)