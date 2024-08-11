from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from keyboards import main
from db import Database
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboards import geolocation, main
from utils import geo, tokens
import requests
from math import ceil

router = Router()
db = Database("./database.db")

@router.message(Command("start"))
async def cmd_start(message: Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        db.get_db()
    await message.answer(
    """Добро пожаловать!
Отправьте Вашу геолокацию по кнопке ниже, напишите город или введите координаты, и я пришлю погоду в данном участке.""", reply_markup=main.main()
    )

@router.message(F.location)
@router.message(Command("test"))
async def weather(message: Message):
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=ru&appid={APIkey}&units=metric'
    # response = requests.get(url=url.format(lon=message.location.longitude, lat=message.location.latitude, APIkey=tokens.owm_token))
    response = requests.get(url=url.format(lon="49.521527", lat="58.260095", APIkey=tokens.owm_token))
    data = response.json()
    print(data)
    wthr = (data['weather'][0]['description']).capitalize()
    temp = (data['main']['temp'])
    wind = (data['wind']['speed'])
    prss = (data['main']['pressure'])
    # wthr_emj = {
    #     'Clouds' : '☁️',
    # }
    await message.answer(f"☁️Осадки: {wthr}\n🌞Температура: {temp} °C\n💨Скорость ветра: {wind} м/с\n🌡Давление: {ceil(prss/1.333)} мм рт. ст.")