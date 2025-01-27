from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram import Router, F
from db import Database
from keyboards import settings, main
from utils import translator
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from datetime import datetime

router = Router()
db = Database("./database.db")

class TimeWeather(StatesGroup):
    time = State()

# НАСТРОЙКИ БОТА: ЯЗЫК, ВРЕМЯ ЕЖЕДНЕВНОЙ ОТПРАВКИ

@router.message(Command("settings"))
async def cmd_settings(message: Message):
    lang = db.get_lang(message.from_user.id)
    answer = translator.get_translation(lang=lang, firstKey='handlers', secondKey='settings', thirdKey='choose_setting')
    await message.answer(answer, reply_markup=settings.choose_setting(lang))

# Язык

@router.callback_query(F.data == "setting_language")
async def cb_change_language(callback: CallbackQuery):
    lang = db.get_lang(callback.from_user.id)
    answer = translator.get_translation(lang=lang, firstKey='handlers', secondKey='settings', thirdKey='choose_language')
    await callback.message.edit_text(answer, reply_markup=settings.choose_language(lang))

@router.callback_query(F.data == "language_ru")
async def cb_lang_ru(callback: CallbackQuery):
    db.set_lang(lang="ru", user_id=callback.from_user.id)
    answer = translator.get_translation(lang="ru", firstKey='handlers', secondKey='settings', thirdKey='language_set_to_ru')
    await callback.message.answer(answer, reply_markup=main.main(lang='ru'))

@router.callback_query(F.data == "language_en")
async def cb_lang_en(callback: CallbackQuery):
    db.set_lang(lang="en", user_id=callback.from_user.id)
    answer = translator.get_translation(lang="en", firstKey='handlers', secondKey='settings', thirdKey='language_set_to_en')
    await callback.message.answer(answer, reply_markup=main.main(lang='en'))

# Время ежедневной отправки погоды

# @router.callback_query(F.data == "setting_time", StateFilter(None))
# async def cb_change_time(callback: CallbackQuery, state: FSMContext):
#     lang = db.get_lang(callback.from_user.id)
#     time = db.get_time(user_id=callback.from_user.id)
#     if time is None:
#         time = translator.get_translation(lang=lang, firstKey='handlers', secondKey='settings', thirdKey='time_is_not_set')
#     answer = translator.get_translation(
#         lang=lang,
#         firstKey='handlers',
#         secondKey='settings',
#         thirdKey='choose_time',
#         time=time
#     )
#     await callback.message.edit_text(answer, reply_markup=settings.choose_time(lang))
#     await state.set_state(TimeWeather.time)

# @router.callback_query(TimeWeather.time)
# async def cb_time(callback: CallbackQuery, state: FSMContext):
#     await callback.answer()
#     lang = db.get_lang(callback.from_user.id)
#     time_str = callback.data

#     if time_str == "setting_time_no_time":
#         answer = translator.get_translation(
#             lang=lang,
#             firstKey='handlers',
#             secondKey='settings',
#             thirdKey='no_time'
#         )
#         db.set_time(time=None, user_id=callback.from_user.id)
#         time = db.get_time(user_id=callback.from_user.id)
#         if time is None:
#             time = translator.get_translation(lang=lang, firstKey='handlers', secondKey='settings', thirdKey='time_is_not_set')
#         msg = translator.get_translation(
#             lang=lang,
#             firstKey='handlers',
#             secondKey='settings',
#             thirdKey='choose_time',
#             time=time
#         )
#         await callback.message.edit_text(msg, reply_markup=settings.choose_time(lang))
#         await callback.answer(answer, reply_markup=main.main(lang=lang))
#         await state.clear()
#         return

#     try:
#         time = datetime.strptime(time_str, '%H:%M')

#         if time.hour < 0 or time.hour > 23 or time.minute < 0 or time.minute > 59:
#             raise ValueError("Time out of range")

#         db.set_time(time=time_str, user_id=callback.from_user.id)
        
#         answer = translator.get_translation(
#             lang=lang,
#             firstKey='handlers',
#             secondKey='settings',
#             thirdKey='choose_time',
#             time=time
#         )
#         await callback.message.edit_reply_markup(answer, reply_markup=main.main(lang=lang))
#         answer = translator.get_translation(
#             lang=lang,
#             firstKey='handlers',
#             secondKey='settings',
#             thirdKey='time_set'
#         )
#         await callback.answer(answer, reply_markup=main.main(lang=lang))
#         await state.clear()
#     except Exception:
#         answer = translator.get_translation(
#             lang=lang,
#             firstKey='handlers',
#             secondKey='settings',
#             thirdKey='invalid_time'
#         )
#         await callback.answer(answer, reply_markup=settings.choose_time(lang))
#         await state.set_state(TimeWeather.time)