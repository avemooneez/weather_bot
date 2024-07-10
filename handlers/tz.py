from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboards import geolocation
from utils import geo
import datetime
import pytz
from db import Database


router = Router()
db = Database("./database.db")

class GetTimeZone(StatesGroup):
    location = State()

@router.message(Command("timezone"), StateFilter(None))
async def cmd_geo(message: Message, state: FSMContext):
    await message.answer(
        "🌍 Для корректной работы боту необходимо знать ваш часовой пояс. Пожалуйста, отправьте вашу геолокацию по кнопке ниже.",
        reply_markup=geolocation.geolocation()
        )
    state.set_state(GetTimeZone.location)

@router.message(F.location, GetTimeZone.location)
async def on_location(message: Message):
    timezone = geo.tz(lon=message.location.longitude, lat=message.location.latitude)
    time = datetime.datetime.now(tz=pytz.timezone(timezone)).strftime("%H:%M")
    await message.answer(f"🌍 Ваш часовой пояс: {timezone}\n"
                         f"🕐 Ваше время: {time}", reply_markup=ReplyKeyboardRemove()
                         )
    db.add_tz(timezone, message.from_user.id)