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
# from apscheduler.schedulers.
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
    wthr_icon = (data['weather'][0]['icon'])
    degree = (data['wind']['deg'])

    wthr_emjs = {
        '01d' : '☀️',
        '01n' : '🌝',
        '02d' : '⛅️',
        '02n' : '⛅️',
        '03d' : '☁️',
        '03n' : '☁️',
        '04d' : '☁️',
        '04n' : '☁️',
        '09d' : '🌧',
        '09n' : '🌧',
        '10d' : '🌦',
        '10n' : '🌦',
        '11d' : '⛈',
        '11n' : '⛈',
        '13d' : '❄️',    
        '13n' : '❄️',
        '50d' : '🌪',
        '50n' : '🌪'
    }
    def get_wind_direction(degree):
        if degree < 0 or degree > 360:
            return "Invalid value"
        
        if degree >= 337.5 or degree < 22.5:
            return "Север"
        elif degree < 67.5:
            return "Северо-восток"
        elif degree < 112.5:
            return "Восток"
        elif degree < 157.5:
            return "Юго-восток"
        elif degree < 202.5:
            return "Юг"
        elif degree < 247.5:
            return "Юго-запад"
        elif degree < 292.5:
            return "Запад"
        elif degree < 337.5:
            return "Северо-запад"

    deg = get_wind_direction(degree)
    wthr_emj = wthr_emjs[wthr_icon]
    await message.answer(f"{wthr_emj} {wthr}\n🌞Температура: {ceil(temp)} °C\n💨Ветер: {wind} м/с | {deg}\n🌡Давление: {ceil(prss/1.333)} мм рт. ст.")
