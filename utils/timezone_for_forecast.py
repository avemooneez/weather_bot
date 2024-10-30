import pytz
import datetime

def formatTimezone(date, timezone_str):
    dt = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    timezone = pytz.timezone(timezone_str)
    timezone_dt = timezone.localize(dt)
    return timezone_dt.strftime('%d.%m.%Y %H:%M')