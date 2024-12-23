from aiogram.types import Message  
from aiogram.filters import Command
from aiogram import Router
from keyboards import main
from db import Database
from keyboards import main
from utils import translator

router = Router()  
db = Database("./database.db") 

# ПЕРЕЗАГРУЗКА БОТА, ВНЕСЕНИЕ В БД НОВЫХ ЮЗЕРОВ

@router.message(Command("start"))  
async def cmd_start(message: Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)

    lang = db.get_lang(message.from_user.id)
    answer = translator.get_translation(lang=lang,
                                        firstKey='handlers', secondKey='start',
                                        thirdKey='welcome')
    
    await message.answer(text=answer, reply_markup=main.main(lang=lang))  

