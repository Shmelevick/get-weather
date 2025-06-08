from dataclasses import dataclass
from datetime import datetime
from typing import TypeAlias
from enum import Enum

from coordinates import Coordinates

Celsius: TypeAlias = int

class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: str
    sunrise: datetime
    sunset: datetime
    city: str

def get_weather(coordinates: Coordinates):
    '''Requests weather in OpenWeather API and returns it'''
    return Weather(
        temperature=20,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat('022-05-04 04:00:00'),
        sunset=datetime.fromisoformat('022-05-04 20:25:00'),
        city='Moscow'
    )

