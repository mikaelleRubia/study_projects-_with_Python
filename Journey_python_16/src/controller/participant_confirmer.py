from typing import Dict
from src.main.models.repositories.participants_repository import ParticipantsRepository


class ParticipantConfirmer:
    def __init__(self, participants_repository: ParticipantsRepository)-> None:
        self.__participants_repository = participants_repository 

    def confirmer(self, participant_id: str)-> Dict:
        try:
            self.__participants_repository.update_participant_is_confirmed(participant_id)
            return { "body": None }, 204
        except Exception as ex:
            return { "body": { "error": "Bad Request", "message": str(ex) } }, 400