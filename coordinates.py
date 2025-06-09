from dataclasses import dataclass
from subprocess import PIPE, Popen

import requests
from bs4 import BeautifulSoup

import config
from exceptions import CantGetCoordinates


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    '''Returns GPS coordinates via Macbook GPS'''
    coordinates = _get_coreloccli_coordinates()
    return _round_coordinates(coordinates)


def _get_coreloccli_coordinates() -> Coordinates:
    process = Popen(['CoreLocationCLI'], stdout=PIPE, stderr=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    if err.decode() or exit_code != 0:
        raise CantGetCoordinates

    try:
        latitude, longitude = map(float, output.decode().strip().split(' '))
    except UnicodeDecodeError:
        raise CantGetCoordinates
    return Coordinates(longitude=longitude, latitude=latitude)


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    latitude, longitude = map(
        lambda c: round(c, 3),
        (coordinates.latitude, coordinates.longitude)
    )
    return Coordinates(longitude=longitude, latitude=latitude)


def parse_gps_coordinates() -> Coordinates:
    '''
    Returns your IP-based coordinates by parsing an external website.
    Make sure your location is accessible by visiting https://mylocation.org/ 
    and that you are not using a VPN.
    '''
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0 Safari/537.36"
        )
    }

    url = 'https://mylocation.org/'

    response = requests.get(url, headers=headers)
    html = response.text
    for parser in ['lxml', 'html.parser']:
        try:
            soup = BeautifulSoup(html, parser)
            latitude = (
                soup.find('td', string="Latitude")
                    .find_next_sibling('td')
                    .text
                    .strip()
            )
            longitude = (
                soup.find('td', string="Longitude")
                    .find_next_sibling('td')
                    .text
                    .strip()
            )
            print(Coordinates(longitude=longitude, latitude=latitude))
            return Coordinates(longitude=longitude, latitude=latitude)
        except AttributeError:
            continue
    raise ValueError(
        "Не удалось найти координаты в HTML"
        "с использованием доступных парсеров."
    )
    

if __name__ == '__main__':
    print(get_gps_coordinates())

