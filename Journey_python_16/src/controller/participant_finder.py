from typing import Dict
from src.main.models.repositories.participants_repository import ParticipantsRepository


class ParticipantFinder:
    def __init__(self, participants_repository: ParticipantsRepository)-> None:
        self.__participants_repository = participants_repository 

    def find( self, participant_id)-> Dict:
        try:
  
            participant = self.__participants_repository.find_participant(participant_id)
            if participant:
                participant_format ={
                    "id" : participant[0], 
                    "trip_id": participant[1],
                    "emails_to_invite_id": participant[2],
                    "name": participant[3],
                    "is_confirmed": participant[4],
                }
                return { "body": { "participant": participant_format } }, 200
            
            return { "body": None }, 200
        
        except Exception as ex:
            return { "body": { "error": "Bad Request", "message": str(ex) } }, 400
        
    def finds_all( self)-> Dict:
        try:
            participants = self.__participants_repository.find_participant_all()

            format_participants = []
            if participants:
                for participant in participants:
                    participant_format ={
                        "id" : participant[0], 
                        "trip_id": participant[1],
                        "emails_to_invite_id": participant[2],
                        "name": participant[3],
                        "is_confirmed": participant[4],

                    }
                    format_participants.append(participant_format)

                return { "body": { "participants": format_participants }}, 200
            
            return { "body": [] }, 200
        
        except Exception as ex:
            return { "body": { "error": "Bad Request", "message": str(ex) } }, 400