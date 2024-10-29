from aiogram.types import Message  
from aiogram.filters import Command
from aiogram import Router, F  
from keyboards import main, timechooser
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

class TimeWeather(StatesGroup):
    time = State()

@router.message(Command("start"), StateFilter(None))  
async def cmd_start(message: Message, state: FSMContext):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        await message.answer(
            "Привет! Ты новый пользователь. Это — телеграм-бот, который может отправлять погоду.\nВведи время, в которое лучше отправлять погоду каждый день или нажми кнопку ниже, чтобы я не отправлял тебе погоду каждый день. Ты всегда можешь изменить своё решение в /settings.",
            reply_markup=timechooser.keyboard()
            )
        await state.set_state(TimeWeather.time)
    else:
        await message.answer(  
        "Добро пожаловать!\nОтправьте Вашу геолокацию по кнопке ниже и я пришлю погоду в данном участке.", reply_markup=main.main()
        )  

@router.message(StateFilter(TimeWeather.time))
async def timechoose(message: Message, state: FSMContext):
    if message.text.lower() == "нет, спасибо":
        await message.answer("Принято!", reply_markup=main.main())
        await state.set_state(None)
    elif not ':' in message.text or not datetime.datetime.strptime(message.text, '%H:%M'):
        await message.answer("Введите корректное время!")
        await state.set_state(TimeWeather.time)        
    else:
        db.add_time(time=message.text, user_id=message.from_user.id)
        await message.answer("Принято!", reply_markup=main.main())
        await state.set_state(None)
        
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
