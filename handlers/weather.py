from aiogram.types import Message
from aiogram import Router, F
from db import Database
from utils import tokens
from utils.start import wthr_emjs, get_wind_direction
import requests
import datetime
import asyncio
from math import ceil  

router = Router()  
db = Database("./database.db") 


@router.message(F.location)
async def weather(message: Message):
    await asyncio.sleep(1)
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=ru&appid={APIkey}&units=metric'
    response = requests.get(url=url.format(lon=f"{message.location.longitude}", lat=f"{message.location.latitude}", APIkey=tokens.owm_token))
    data = response.json()
    print(data)
    wthr = (data['weather'][0]['description']).capitalize()
    temp = (data['main']['temp'])  
    wind = (data['wind']['speed']) 
    prss = (data['main']['pressure'])
    wthr_icon = (data['weather'][0]['icon'])
    degree = (data['wind']['deg']) 
    loc = (data['name'])   
    deg = get_wind_direction(degree)
    wthr_emj = wthr_emjs[wthr_icon]
    await message.answer(f"Локация: {loc} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n{wthr_emj}{wthr}\n🌞Температура: {ceil(temp)} °C\n💨Ветер: {wind} м/с | {deg}\n🌡Давление: {ceil(prss/1.333)} мм рт. ст.")
