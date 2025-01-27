translations = {
    'en' : {
        'handlers' : {
            'forecast' : {
                'get_location' : 'Please send your location using the button below',
                'forecast_msg' : '{date}\n{weather_emoji}{wthr}\n🌞Temperature: {temp} °C\n💨Wind: {wind} m/s, {degree}\n🌡Pressure: {pressure} mmHg\n\n',
                'answer' : 'Location: {loc} \n\n',
            },
            'start' : {
                'welcome' : 'Welcome!\nSend your geolocation using the button below and I will send you the weather in this area\n\nUsing the button below or the name of the city, I will send you the weather.\n/settings — bot settings. There you can configure the language of the bot, as well as the time of daily weather sending.\n/forecast — I will send you the weather forecast for the next 24 hours'
            },
            'weather' : {
                'answer' : 'Location: {loc} | {date}\n\n{weather_emoji}{wthr}\n🌞Temperature: {temp} °C\n💨Wind: {wind} m/s, {degree}\n🌡Pressure: {pressure} mmHg'
            },
            'settings' : {
                'choose_setting' : 'Choose a setting using buttons below',
                'choose_language' : 'Below are the available languages of the bot',
                'language_set_to_en' : 'The bot language has been successfully changed. Please, restart the bot — /start.',
                'choose_time' : 'Set time: {time}\n\nEnter the time when it is best to send the weather every day or click the button below so that I do not send you the weather every day',
                'no_time' : 'OK!',
                'time_set' : 'The time has been successfully changed.',
                'invalid_time' : "Incorrect time entered! Please try again or use the button below so I don't send you the weather every day",
                'time_is_not_set' : 'Not set',
            }
        },
        'keyboards' : {
            'geo' : {
                'loc' : 'Send your location'
            },
            'main' : {
                'loc' : 'Send your location'
            },
            'timechooser' : {
                'no_time' : 'No, thanks'
            },
            'settings' : {
                'choose_setting_time' : 'Daily weather sending time',
                'choose_setting_language' : 'Bot language',
                'choose_language_ru' : 'Русский',
                'choose_language_en' : 'English',
                'no_time' : 'No, thanks'
            }
        },
        'utils' : {
            'weather' : {
                'north' : 'N',
                'northeast' : 'NE',
                'east' : 'E',
                'southeast' : 'SE',
                'south' : 'S',
                'southwest' : 'SW',
                'west' : 'W',
                'northwest' : 'NW'
            }
        }
    },
    'ru' : {
        'handlers' : {
            'forecast' : {
                'get_location' : 'Пожалуйста, отправьте ваше местоположение по кнопке ниже',
                'forecast_msg' : '{date}\n{weather_emoji}{wthr}\n🌞Температура: {temp} °C\n💨Ветер: {wind} м/с | {degree}\n🌡Давление: {pressure} мм рт. ст.\n\n',
                'answer' : 'Локация: {loc} \n\n',
            },
            'start' : {
                'welcome' : 'Добро пожаловать!\nОтправьте Вашу геолокацию по кнопке ниже и я пришлю погоду в данном участке\n\nПо кнопке ниже или по названию города — пришлю погоду.\n/settings — настройки бота. Там Вы можете настроить язык бота, а также время ежедневной отправки погоды.\n/forecast — отправлю прогноз погоды на ближайшие сутки'
            },
            'weather' : {
                'answer' : 'Локация: {loc} | {date}\n\n{weather_emoji}{wthr}\n🌞Температура: {temp} °C\n💨Ветер: {wind} м/с | {degree}\n🌡Давление: {pressure} мм рт. ст.'
            },
            'settings' : {
                'choose_setting' : 'Выберите настройку с помощью кнопок ниже',
                'choose_language' : 'Ниже представлены доступные языки бота',
                'language_set_to_ru' : 'Язык бота был успешно изменен. Пожалуйста, перезагрузите бота командой /start.',
                'choose_time' : 'Время на данный момент: {time}\n\nВведите время, когда лучше отправлять погоду каждый день или нажмите на кнопку ниже, чтобы я не отправлял вам погоду каждый день',
                'no_time' : 'Принято!',
                'time_set' : 'Время было успешно изменено',
                'invalid_time' : 'Введено некорректное время! Пожалуйста, попробуйте снова или воспользуйтесь кнопкой ниже, чтобы я не присылал вам погоду каждый день',
                'time_is_not_set' : 'Не выбрано'
            }
        },
        'keyboards' : {
            'geo' : {
                'loc' : 'Отправить свою геолокацию'
            },
            'main' : {
                'loc' : 'Отправить свою геолокацию'
            },
            'timechooser' : {
                'no_time' : 'Нет, спасибо'
            },
            'settings' : {
                'choose_setting_time' : 'Время ежедненой отправки погоды',
                'choose_setting_language' : 'Язык бота',
                'choose_language_ru' : 'Русский',
                'choose_language_en' : 'English',
                'no_time' : 'Нет, спасибо'
            }
        },
        'utils' : {
            'weather' : {
                'north' : 'Север',
                'northeast' : 'Северо-восток',
                'east' : 'Восток',
                'southeast' : 'Юго-восток',
                'south' : 'Юг',
                'southwest' : 'Юго-запад',
                'west' : 'Запад',
                'northwest' : 'Северо-запад'
            }
        }
    }
}

def get_translation(lang: str, firstKey: str, secondKey: str, thirdKey: str, **kwargs):
    return translations.get(lang, {}).get(firstKey, {}).get(secondKey, {}).get(thirdKey, {}).format(**kwargs)