import os

from dotenv import load_dotenv

load_dotenv()


USE_ROUNDED_COORDS = True

OPENWEATHER_API = os.getenv('OPENWEATHER_API_KEY')
if OPENWEATHER_API is None:
    raise RuntimeError('did not get OPENWEATHER_API')

OPENWEATHER_URL = (
    'https://api.openweathermap.org/data/2.5/weather?'
    'lat={latitude}&lon={longitude}&'
    'appid=' + OPENWEATHER_API + '&lang=ru&units=metric'
)