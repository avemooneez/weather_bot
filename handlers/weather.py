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
from utils import translator

router = Router()  
db = Database("./database.db") 

# ОТПРАВКА ПОГОДЫ СЕЙЧАС

@router.message(F.location)
async def getWeather(message: Message):
    await asyncio.sleep(1)
    timezone = tz(lon=message.location.longitude, lat=message.location.latitude)
    lang = db.get_lang(message.from_user.id)
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang={lang}&appid={APIkey}&units=metric'
    response = requests.get(url=url.format(lon=f"{message.location.longitude}", lat=f"{message.location.latitude}", APIkey=owm_token, lang=lang))
    data = response.json()
    print(data)
    wthr = (data['weather'][0]['description']).capitalize()
    temp = (data['main']['temp'])  
    wind = (data['wind']['speed']) 
    prss = (data['main']['pressure'])
    wthr_icon = (data['weather'][0]['icon'])
    degree = (data['wind']['deg']) 
    loc = (data['name'])   
    deg = weather.get_wind_direction(degree, lang)
    wthr_emj = weather.wthr_emjs[wthr_icon]
    
    answer = translator.get_translation(lang=lang, firstKey='handlers', secondKey='weather', thirdKey='answer', loc=loc,
                                        date=datetime.now(tz=pytz.timezone(timezone)).strftime('%d.%m.%Y %H:%M'),
                                        weather_emoji=wthr_emj, wthr=wthr, temp=ceil(temp), wind=wind, degree=deg, pressure=ceil(prss/1.333))
    await message.answer(answer)

@router.message(F.text)
async def getWeatherByText(message: Message):
    await asyncio.sleep(1)
    lang = db.get_lang(message.from_user.id)
    url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&lang={lang}&appid={APIkey}&units=metric'
    response = requests.get(url=url.format(city=message.text, APIkey=owm_token, lang=lang))
    print(url.format(city=F.text, APIkey=owm_token, lang=lang))
    data = response.json()
    print(data)
    if data['cod'] == 200:
        wthr = (data['weather'][0]['description']).capitalize()
        temp = (data['main']['temp'])  
        wind = (data['wind']['speed']) 
        prss = (data['main']['pressure'])
        wthr_icon = (data['weather'][0]['icon'])
        degree = (data['wind']['deg']) 
        loc = (data['name'])
        timezone = int(data['timezone'])
        deg = weather.get_wind_direction(degree, lang)
        wthr_emj = weather.wthr_emjs[wthr_icon]
        
        answer = translator.get_translation(lang=lang, firstKey='handlers', secondKey='weather', thirdKey='answer', loc=loc,
                                            date=datetime.now(tz=pytz.FixedOffset(timezone // 60)).strftime('%d.%m.%Y %H:%M'),
                                            weather_emoji=wthr_emj, wthr=wthr, temp=ceil(temp), wind=wind, degree=deg, pressure=ceil(prss/1.333))
        await message.answer(answer)
    else:
        await message.answer('Unknown error.')