from typing import Dict
import uuid
from src.main.models.repositories.participants_repository import ParticipantsRepository


class ParticipantCreator:
    def __init__(self, participants_repository: ParticipantsRepository)-> None:
        self.__participants_repository = participants_repository 

    def create( self, body)-> Dict:
        try:
            participants_id = str(uuid.uuid4())
            participants_infos = {**body, "id": participants_id}
            self.__participants_repository.create_participant(participants_infos)

            return { "body": { "participants_Id": participants_id } }, 201
        
        except Exception as ex:
            return { "body": { "error": "Bad Request", "message": str(ex) } }, 400