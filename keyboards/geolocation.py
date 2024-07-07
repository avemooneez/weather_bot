from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def geolocation() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Отправить свою геолокацию", request_location=True)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
