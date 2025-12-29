
from typing import Dict
from src.main.models.repositories.trips_repository import TripsRepository


class TripFinder:
    def __init__(self, trip_repository: TripsRepository)-> None:
        self.__trip_repository = trip_repository 


    def find_trip_details(self, trip_id: str)-> Dict:
        try:
            trip = self.__trip_repository.find_trip(trip_id)
            if not trip: raise Exception("No Trip Found")

            return { "body":{
                        "trip":{
                            "id": trip[0],
                            "destination": trip[1],
                            "start_date": trip[2],
                            "end_date": trip[3], 
                            "owner_name": trip[4],
                            "owner_email":trip[5],
                            "status":trip[6]
                    }
                }
            }, 200
        except Exception as ex:
            return { "body": { "error": "Bad Request", "message": str(ex) } }, 400