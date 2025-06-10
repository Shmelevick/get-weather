from dataclasses import dataclass
from subprocess import PIPE, Popen


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


if __name__ == '__main__':
    print(get_gps_coordinates())

