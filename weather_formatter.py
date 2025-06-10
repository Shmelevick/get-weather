from weather_api_service import Weather
from datetime import datetime


def format_weather(weather: Weather) -> str:
    '''Formats weather data into a string'''
    return (
        f'{weather.city}, {datetime.now().strftime('%d.%m.%Y')}\n'
        f'Время: {datetime.now().strftime('%H:%M')}\n'
        f'температура {weather.temperature}°C, '
        f'{weather.weather_type.lower()}\n'
        f'Восход: {weather.sunrise.strftime('%H:%M')}\n'
        f'Закат: {weather.sunset.strftime('%H:%M')}\n'
    )


if __name__ == '__main__':
    from datetime import datetime

    from weather_api_service import WeatherType
    print(
        format_weather(
            Weather(
                temperature=66,
                weather_type=WeatherType.CLEAR,
                sunrise=datetime.fromisoformat('2022-05-03 04:00:00'),
                sunset=datetime.fromisoformat('2022-05-03 20:25:00'),
                city='Moscow'
            )
        )
    )