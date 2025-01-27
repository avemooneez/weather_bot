from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils import translator

def choose_setting(lang) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    
    # for key in ['time', 'language']:
    #     kb.button(text=translator.get_translation(
    #         lang=lang, firstKey='keyboards', secondKey='settings',
    #         thirdKey='choose_setting_' + key), callback_data='setting_' + key)
    kb.button(text=translator.get_translation(
        lang=lang, firstKey='keyboards',
        secondKey='settings', thirdKey='choose_setting_language'
        ), callback_data='setting_language')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)

# def choose_time(lang) -> InlineKeyboardMarkup:
#     kb = InlineKeyboardBuilder()
    
#     kb.button(text=translator.get_translation(
#         lang=lang, firstKey='keyboards', secondKey='timechooser',
#         thirdKey='no_time'), callback_data='setting_time_no_time')
#     kb.adjust(1)
#     return kb.as_markup(resize_keyboard=True)

def choose_language(lang) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    
    for key in ['ru', 'en']:
        kb.button(text=translator.get_translation(
            lang=lang, firstKey='keyboards', secondKey='settings',
            thirdKey='choose_language_' + key),
                  callback_data='language_' + key)
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
