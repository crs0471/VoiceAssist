import pyowm
token = "" #Your token goes here
# own= pyowm.OWM(token).weather_manager()

def get_weather(*args, **kwargs):
    return f"Currently, the temperature is {0} degrees"

    zip_code = "10001" #Update this to your zip code
    weather = own.weather_at_zip_code(zip_code, 'US').weather
    temperature = int(round(weather.temperature(unit='fahrenheit')['temp'], 0))
    return f"Currently, the temperature is {temperature} degrees"