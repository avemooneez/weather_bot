from typing import Any, Awaitable, Callable, Dict
from aiogram.types import Message, TelegramObject
from aiogram import BaseMiddleware
from db import Database

db = Database("./database.db")

class UserExists(BaseMiddleware):

    def __init__(self):
        pass

    async def __call__(self,
                       handler: Callable[[TelegramObject,Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]
                       ) -> Any:
        if not db.user_exists(event.from_user.id):
            db.add_user(event.from_user.id)
        return await handler(event, data)
