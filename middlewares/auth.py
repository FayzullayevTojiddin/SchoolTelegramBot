from aiogram import BaseMiddleware
from aiogram.types import Update
from typing import Callable, Dict, Any, Awaitable
from models.user import User

from aiogram.fsm.context import FSMContext

class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        state: FSMContext = data['state']
        current_state = await state.get_state()
        print(current_state)
        if event.message:
            user_from = event.message.from_user

        elif event.callback_query:
            user_from = event.callback_query.from_user

        user = User.get_user(user_from.id)
        if not user:
            User.create(
                user_id = user_from.id, 
                first_name = user_from.first_name, 
                last_name = user_from.last_name, 
                username = user_from.username
            )

        return await handler(event, data)