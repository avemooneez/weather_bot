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
def get_wind_direction(degree):
    if degree < 0 or degree > 360:
        return "Invalid value" 
    
    if degree >= 337.5 or degree < 22.5:
        return "Север" 
    elif degree < 67.5:
        return "Северо-восток" 
    elif degree < 112.5:   
        return "Восток"
    elif degree < 157.5:   
        return "Юго-восток"
    elif degree < 202.5:   
        return "Юг"
    elif degree < 247.5:   
        return "Юго-запад" 
    elif degree < 292.5:   
        return "Запад" 
    elif degree < 337.5:   
        return "Северо-запад"  
