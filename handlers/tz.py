from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram import Router, F
from keyboards import geolocation
from utils import geo
import datetime
import pytz
from db import Database


router = Router()
db = Database("./database.db")

@router.message(Command("geo"))
async def cmd_geo(message: Message):
    await message.answer(
        "🌍 Для корректной работы боту необходимо знать ваш часовой пояс. Пожалуйста, отправьте вашу геолокацию по кнопке ниже.",
        reply_markup=geolocation.geolocation()
        )

@router.message(F.location)
async def on_location(message: Message):
    timezone = geo.tz(lon=message.location.longitude, lat=message.location.latitude)
    time = datetime.datetime.now(tz=pytz.timezone(timezone)).strftime("%H:%M")
    await message.answer(f"🌍 Ваш часовой пояс: {timezone}\n"
                         f"🕐 Ваше время: {time}", reply_markup=ReplyKeyboardRemove()
                         )
    db.add_tz(timezone, message.from_user.id)