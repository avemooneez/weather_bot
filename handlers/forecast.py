from aiogram.types import Message  
from aiogram.filters import Command
from aiogram import Router, F  
from keyboards import main
from db import Database
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboards import main
from utils import tokens, timezone_for_forecast, translator
from utils.geo import tz
from utils.weather import wthr_emjs, get_wind_direction
import requests
import asyncio
from math import ceil  

router = Router()  
db = Database("./database.db") 

class ForecastStates(StatesGroup):
    forecast = State()
   
@router.message(Command("forecast"), StateFilter(None))
async def cmd_forecast(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    answer = translator.get_translation(lang=lang,firstKey='handlers', secondKey='forecast', thirdKey='get_location')
    await message.answer(text=answer, reply_markup=main.main(lang=lang))
    await state.set_state(ForecastStates.forecast)

@router.message(StateFilter(ForecastStates.forecast))
async def forecast(message: Message, state: FSMContext):
    await asyncio.sleep(1)
    lang = db.get_lang(message.from_user.id)
    timezone_str = tz(lon=message.location.longitude, lat=message.location.latitude)
    url = 'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&lang={lang}&appid={APIkey}&units=metric'
    response = requests.get(url=url.format(lon=f"{message.location.longitude}", lat=f"{message.location.latitude}", APIkey=tokens.owm_token, lang=lang))
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
        dt = timezone_for_forecast.formatTimezone(da['dt_txt'], timezone_str)
        deg = get_wind_direction(degree, lang)
        msg += translator.get_translation(lang=lang, firstKey='handlers',
                                          secondKey='forecast', thirdKey='forecast_msg', date=dt,
                                          weather_emoji=wthr_emjs[wthr_icon], wthr=wthr, temp=ceil(temp),
                                          wind=wind, degree=deg, pressure=ceil(prss/1.333))
        answer = translator.get_translation(lang=lang, firstKey='handlers',
                                            secondKey='forecast', thirdKey='answer', loc=loc)
    await message.answer(answer + msg)
    await state.set_state(None)
