from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float

def get_gps_coordinates() -> Coordinates:
    '''Returns your coordinates via MacBook GPS'''
    return Coordinates(longitude=10, latitude=20)