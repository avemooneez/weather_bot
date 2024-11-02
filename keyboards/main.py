from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from utils import translator

def main(lang) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=translator.get_translation(lang=lang, firstKey='keyboards', secondKey='main',
                                              thirdKey='loc'), request_location=True)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
