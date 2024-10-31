from aiogram.types import Message  
from aiogram.filters import Command
from aiogram import Router, F  
from keyboards import main, timechooser
from db import Database
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboards import main
from datetime import datetime

router = Router()  
db = Database("./database.db") 

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
    elif not ':' in message.text or not datetime.strptime(message.text, '%H:%M'):
        await message.answer("Введите корректное время!")
        await state.set_state(TimeWeather.time)        
    else:
        db.add_time(time=message.text, user_id=message.from_user.id)
        await message.answer("Принято!", reply_markup=main.main())
        await state.set_state(None)
