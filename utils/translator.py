translations = {
    'en' : {
        'handlers' : {
            'forecast' : {
                'get_location' : 'Please send your location using the button below',
                'forecast_msg' : '{date}\n{weather_emoji}{wthr}\n🌞Temperature: {ceiled_temp} °C\n💨Wind: {wind} m/s, {degree}\n🌡Pressure: {ceiled_pressure} mmHg\n\n',
                'answer' : 'Location: {loc} \n\n',
            },
            'start' : {
                'welcome_new_user' : 'Hello! You are a new user. This is a telegram bot that can send the weather.\nEnter the time when it is better to send the weather every day or click the button below so that I do not send you the weather every day. You can always change your mind in /settings.',
                'welcome' : 'Welcome!\nSend your geolocation using the button below and I will send you the weather in this area.',
                'answer_is_given' : 'OK!',
                'incorrect_time' : 'Please enter a valid time!'
            },
            'weather' : {
                'answer' : 'Location: {loc} | {date}\n\n{weather_emoji}{wthr}\n🌞Temperature: {ceiled_temp} °C\n💨Wind: {wind} m/s, {degree}\n🌡Pressure: {ceiled_pressure} mmHg'
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
            
        },
        'keyboards' : {
            
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
    pass