from aiogram.types import Message
from aiogram import Router, F
from db import Database
from utils.geo import tz
from utils.tokens import owm_token
from utils import weather
import requests
from datetime import datetime
import asyncio
from math import ceil  
import pytz

router = Router()  
db = Database("./database.db") 


@router.message(F.location)
async def getWeather(message: Message):
    await asyncio.sleep(1)
    timezone = tz(lon=message.location.longitude, lat=message.location.latitude)
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=ru&appid={APIkey}&units=metric'
    response = requests.get(url=url.format(lon=f"{message.location.longitude}", lat=f"{message.location.latitude}", APIkey=owm_token))
    data = response.json()
    print(data)
    wthr = (data['weather'][0]['description']).capitalize()
    temp = (data['main']['temp'])  
    wind = (data['wind']['speed']) 
    prss = (data['main']['pressure'])
    wthr_icon = (data['weather'][0]['icon'])
    degree = (data['wind']['deg']) 
    loc = (data['name'])   
    deg = weather.get_wind_direction(degree)
    wthr_emj = weather.wthr_emjs[wthr_icon]
    await message.answer(f"Локация: {loc} | {datetime.now(tz=pytz.timezone(timezone)).strftime('%d.%m.%Y %H:%M')}\n\n{wthr_emj}{wthr}\n🌞Температура: {ceil(temp)} °C\n💨Ветер: {wind} м/с | {deg}\n🌡Давление: {ceil(prss/1.333)} мм рт. ст.")
