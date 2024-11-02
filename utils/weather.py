from utils import translator

wthr_emjs = {  
    '01d' : '☀️',  
    '01n' : '🌝',  
    '02d' : '⛅️',  
    '02n' : '⛅️',  
    '03d' : '☁️',  
    '03n' : '☁️',  
    '04d' : '☁️',  
    '04n' : '☁️',  
    '09d' : '🌧',  
    '09n' : '🌧',  
    '10d' : '🌦',  
    '10n' : '🌦',  
    '11d' : '⛈',  
    '11n' : '⛈',  
    '13d' : '❄️',      
    '13n' : '❄️',  
    '50d' : '🌪',  
    '50n' : '🌪'   
}  
def get_wind_direction(degree, lang):
    if degree < 0 or degree > 360:
        return "Invalid value" 
    
    if degree >= 337.5 or degree < 22.5:
        return translator.get_translation(lang=lang, firstKey='utils', secondKey='weather', thirdKey='north')
    elif degree < 67.5:
        return translator.get_translation(lang=lang, firstKey='utils', secondKey='weather', thirdKey='northwest')
    elif degree < 112.5:   
        return translator.get_translation(lang=lang, firstKey='utils', secondKey='weather', thirdKey='west')
    elif degree < 157.5:   
        return translator.get_translation(lang=lang, firstKey='utils', secondKey='weather', thirdKey='southwest')
    elif degree < 202.5:   
        return translator.get_translation(lang=lang, firstKey='utils', secondKey='weather', thirdKey='south')
    elif degree < 247.5:   
        return translator.get_translation(lang=lang, firstKey='utils', secondKey='weather', thirdKey='southeast')
    elif degree < 292.5:   
        return translator.get_translation(lang=lang, firstKey='utils', secondKey='weather', thirdKey='east')
    elif degree < 337.5:   
        return translator.get_translation(lang=lang, firstKey='utils', secondKey='weather', thirdKey='northeast')
