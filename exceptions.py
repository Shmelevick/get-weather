class CantGetCoordinates(Exception):
    """The program can't retrieve current GPS coordinates"""
    
class ApiServiceError(Exception):
    """Проблема с API"""