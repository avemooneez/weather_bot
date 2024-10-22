from aiogram.types import Message  
from aiogram.filters import Command
from aiogram import Router, F  
from keyboards import main 
from db import Database
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards import main
from utils import tokens
from utils.start import wthr_emjs, get_wind_direction
import requests
import datetime
import asyncio
from math import ceil  

router = Router()  
db = Database("./database.db") 

@router.message(Command("start"))  
async def cmd_start(message: Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        db.get_db()
    await message.answer(  
    "Добро пожаловать!\nОтправьте Вашу геолокацию по кнопке ниже и я пришлю погоду в данном участке.", reply_markup=main.main()
    )  

@router.message(F.location)
async def weather(message: Message):
    await asyncio.sleep(1)
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=ru&appid={APIkey}&units=metric'
    response = requests.get(url=url.format(lon=f"{message.location.longitude}", lat=f"{message.location.latitude}", APIkey=tokens.owm_token))
    data = response.json() 
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

@router.message(Command("forecast"))
async def cmd_forecast(message: Message):
    await asyncio.sleep(1)
    url = 'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&lang=ru&appid={APIkey}&units=metric'
    response = requests.get(url=url.format(lon="49.521527", lat="58.260095", APIkey=tokens.owm_token))
    data = response.json()
    loc = (data['city']['name'])
    msg = ""
    for i in range(9):
        da = data['list'][i]
        wthr = (da['weather'][0]['description']).capitalize()
        temp = (da['main']['temp'])  
        wind = (da['wind']['speed']) 
        prss = (da['main']['pressure'])
        wthr_icon = (da['weather'][0]['icon'])
        degree = (da['wind']['deg'])
        # date = (da['dt_txt'])[:-3] 
        date = datetime.datetime.strptime(da['dt_txt'], '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y %H:%M')
        deg = get_wind_direction(degree)
        msg += f"{date}\n{wthr_emjs[wthr_icon]}{wthr}\n🌞Температура: {ceil(temp)} °C\n💨Ветер: {wind} м/с | {deg}\n🌡Давление: {ceil(prss/1.333)} мм рт. ст.\n\n"
    await message.answer(f"Локация: {loc} \n\n" + msg)