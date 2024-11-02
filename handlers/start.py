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
from utils import translator

router = Router()  
db = Database("./database.db") 

class TimeWeather(StatesGroup):
    time = State()

@router.message(Command("start"), StateFilter(None))  
async def cmd_start(message: Message, state: FSMContext):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        lang = db.get_lang(message.from_user.id)
        answer = translator.get_translation(lang=lang,
                                            firstKey='handlers', secondKey='start',
                                            thirdKey='welcome_new_user')
        
        await message.answer(text=answer, reply_markup=timechooser.keyboard(lang=lang)
            )
        await state.set_state(TimeWeather.time)
    else:
        lang = db.get_lang(message.from_user.id)
        answer = translator.get_translation(lang=lang,
                                            firstKey='handlers', secondKey='start',
                                            thirdKey='welcome')
        
        await message.answer(text=answer, reply_markup=main.main(lang=lang))  

@router.message(StateFilter(TimeWeather.time))
async def timechoose(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    if message.text.lower() == "нет, спасибо" or message.text.lower() == "no, thanks":
        answer = translator.get_translation(lang=lang,
                                            firstKey='handlers', secondKey='start',
                                            thirdKey='answer_is_given')
        
        await message.answer(text=answer, reply_markup=main.main(lang=lang))
        await state.set_state(None)
    elif not ':' in message.text or not datetime.strptime(message.text, '%H:%M'):
        answer = translator.get_translation(lang=lang,
                                            firstKey='handlers', secondKey='start',
                                            thirdKey='incorrect_time')
        
        await message.answer(text=answer)
        await state.set_state(TimeWeather.time)        
    else:
        db.add_time(time=message.text, user_id=message.from_user.id)
        answer = translator.get_translation(lang=lang,
                                            firstKey='handlers', secondKey='start',
                                            thirdKey='answer_is_given')
        
        await message.answer(text=answer, reply_markup=main.main(lang=lang))
        await state.set_state(None)
