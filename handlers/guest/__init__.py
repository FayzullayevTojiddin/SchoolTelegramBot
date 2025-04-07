from aiogram import Router
from .start_message import router as start_message_router
from .main_messages import router as main_message_router
from .back_message import router as back_message_router
from .course_handler import router as course_handler_router
from .teacher_handler import router as teacher_handler_router
from .feedback_handler import router as feedback_handler_router
from .login_message import router as login_handler_router
from .quit import router as quit_handler_router

router = Router(name=__name__)

router.include_routers(
    start_message_router, 
    main_message_router, 
    back_message_router, 
    course_handler_router, 
    teacher_handler_router, 
    feedback_handler_router,
    login_handler_router,
    quit_handler_router,
)