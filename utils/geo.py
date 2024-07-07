import timezonefinder

def tz(lon, lat):
    tf = timezonefinder.TimezoneFinder()
    timezone_str = tf.certain_timezone_at(lat=lat, lng=lon)
    return timezone_str