from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboards import geolocation, main
from utils import geo
from datetime import datetime
import pytz
import asyncio
from db import Database


router = Router()
db = Database("./database.db")

class GetTimeZone(StatesGroup):
    location = State()

@router.message(StateFilter(None), Command("timezone"))
async def cmd_geo(message: Message, state: FSMContext):
    await message.answer(
        "🌍 Для корректной работы боту необходимо знать ваш часовой пояс. Пожалуйста, отправьте вашу геолокацию по кнопке ниже.",
        reply_markup=geolocation.geolocation()
        )
    await state.set_state(GetTimeZone.location)

@router.message(GetTimeZone.location)
async def on_location(message: Message, state: FSMContext):
    timezone = geo.tz(lon=message.location.longitude, lat=message.location.latitude)
    time = datetime.now(tz=pytz.timezone(timezone)).strftime("%H:%M")
    await message.answer(f"🌍 Ваш часовой пояс: {timezone}\n"
                         f"🕐 Ваше время: {time}", reply_markup=main.main()
                         )
    db.add_tz(timezone, message.from_user.id)
    await asyncio.sleep(1.5)
    await message.answer("Отправьте Вашу геолокацию по кнопке ниже и я пришлю погоду в данном участке.",
                         reply_markup=main.main())
    await state.set_state(None)
