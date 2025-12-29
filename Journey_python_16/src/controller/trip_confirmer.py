from typing import Dict
from src.main.models.repositories.trips_repository import TripsRepository


class TripConfirmer:
    def __init__(self, trip_repository: TripsRepository)-> None:
        self.__trip_repository = trip_repository 

    def confirmer(self, trip_id: str)-> Dict:
        try:
            self.__trip_repository.update_trip_status(trip_id)
            return { "body": None }, 204
        except Exception as ex:
            return { "body": { "error": "Bad Request", "message": str(ex) } }, 400