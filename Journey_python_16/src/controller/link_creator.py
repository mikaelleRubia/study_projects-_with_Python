from typing import Dict
import uuid
from src.main.models.repositories.links_repository import LinkRepository


class LinkCreator:
    def __init__(self, link_repository: LinkRepository)-> None:
        self.__link_repository = link_repository 

    def create ( self, body, trip_id)-> Dict:
        try:
            link_id = str(uuid.uuid4())
            link_infos = {**body, "id": link_id, "trip_id": trip_id }
            self.__link_repository.create_links(link_infos)

            return { "body": { "linkId": link_id } }, 201
        
        except Exception as ex:
            return { "body": { "error": "Bad Request", "message": str(ex) } }, 400