from typing import Dict
import uuid
from src.main.models.repositories.links_repository import LinkRepository


class LinkFinder:
    def __init__(self, link_repository: LinkRepository)-> None:
        self.__link_repository = link_repository 

    def find( self, trip_id)-> Dict:
        try:
            
            links = self.__link_repository.find_trip_id_links(trip_id)
            format_links = []
            for link in links:
                link_format ={
                    "id" : link[0], 
                    "trip_id" : link[1], 
                    "link" : link[2], 
                    "title" : link[3],
                }
                format_links.append(link_format)

            return { "body": { "links": format_links } }, 200
        
        except Exception as ex:
            return { "body": { "error": "Bad Request", "message": str(ex) } }, 400