from typing import Dict
import uuid

from src.main.models.repositories.trips_repository import TripsRepository
from src.main.models.repositories.emails_to_invite_repository import EmailToInviteRepository



class TripCreator:
    def __init__(self, trip_repository: TripsRepository, emails_repositories: EmailToInviteRepository)-> None:
        self.__trip_repository = trip_repository 
        self.__emails_repositories = emails_repositories

    def create(self, body) -> Dict:
        try:
            emails = body.get("emails_to_invite")
            trip_id = str(uuid.uuid4())
            trip_infos = {**body, "id": trip_id }
            self.__trip_repository.create_trip(trip_infos)

            if emails:
                for email in emails:
                    email_id = str(uuid.uuid4())
                    body_email ={
                        "id": email_id,
                        "trip_id": trip_id,
                        "email": email
                    }
                    email_infos = {**body_email}
                    self.__emails_repositories.create_emails_to_invite(email_infos) 
            
            return { "body": { "tripId": trip_id } }, 201
        
        except Exception as ex:
            return { "body": { "error": "Bad Request", "message": str(ex) } }, 400