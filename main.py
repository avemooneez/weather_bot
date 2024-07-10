import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from utils import tokens
from handlers import start, tz
from middlewares import userexists
from db import Database


async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

    db = Database("./database.db")
    db.start()
    
    bot = Bot(token=tokens.bot_token)
    dp = Dispatcher()
    
    dp.include_routers(
        start.router,
        tz.router
        )
    
    dp.message.middleware(userexists)
    dp.message.filter(F.chat.type.in_({"private"}))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())