from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from keyboards import main
from db import Database
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboards import geolocation, main
from utils import geo

router = Router()
db = Database("./database.db")

@router.message(Command("start"))
async def cmd_start(message: Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        db.get_db()
    await message.answer("Добро пожаловать!\nОтправьте Вашу геолокацию по кнопке ниже, напишите город или введите координаты, и я пришлю погоду в данном участке.",
                         reply_markup=main.main())
