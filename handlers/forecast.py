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

class ForecastStates(StatesGroup):
    forecast = State()
   
@router.message(Command("forecast"), StateFilter(None))
async def cmd_forecast(message: Message, state: FSMContext):
    await message.answer("Пожалуйста, отправьте ваше местоположение по кнопке ниже", reply_markup=main.main())
    await state.set_state(ForecastStates.forecast)

@router.message(StateFilter(ForecastStates.forecast))
async def forecast(message: Message, state: FSMContext):
    
    await asyncio.sleep(1)
    url = 'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&lang=ru&appid={APIkey}&units=metric'
    response = requests.get(url=url.format(lon=f"{message.location.longitude}", lat=f"{message.location.latitude}", APIkey=tokens.owm_token))
    data = response.json()
    print(data)
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
        date = datetime.datetime.strptime(da['dt_txt'], '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y %H:%M')
        deg = get_wind_direction(degree)
        msg += f"{date}\n{wthr_emjs[wthr_icon]}{wthr}\n🌞Температура: {ceil(temp)} °C\n💨Ветер: {wind} м/с | {deg}\n🌡Давление: {ceil(prss/1.333)} мм рт. ст.\n\n"
    await message.answer(f"Локация: {loc} \n\n" + msg)
    await state.set_state(None)
