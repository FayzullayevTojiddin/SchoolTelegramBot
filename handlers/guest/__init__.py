from aiogram import Router
from .course_handler import router as course_handler_router
from .teacher_handler import router as teacher_handler_router
from .feedback_handler import router as feedback_handler_router
from .login_message import router as login_handler_router
from .quit import router as quit_handler_router

router = Router(name=__name__)

router.include_routers(
    course_handler_router, 
    teacher_handler_router, 
    feedback_handler_router,
    login_handler_router,
    quit_handler_router,
)