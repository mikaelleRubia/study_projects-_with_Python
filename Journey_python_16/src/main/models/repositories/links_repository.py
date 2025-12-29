from sqlite3 import Connection
from typing import Dict, List, Tuple

class LinkRepository:
    def __init__(self, conn: Connection) -> None:
            if conn is None:
                raise Exception("Conexão com o banco de dados não pode ser None")
            self.__conn = conn


    def create_links(self, links: Dict):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO links 
                (id, trip_id, link, title)
            VALUES (?, ?, ?, ?)
            ''',(links["id"], 
               links["trip_id"], 
                links["link"], 
                links["title"], 
            )
            
        )
        self.__conn.commit()

    def find_links(self, link_id: str)-> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM 'links' WHERE id =? 
            ''', (link_id, )
        )
        link = cursor.fetchone()
        return link
    
    def find_trip_id_links(self, trip_id: str)-> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM 'links' WHERE trip_id =? 
            ''', (trip_id, )
        )
        links = cursor.fetchall()
        return links
    
    def find_links_all(self)-> List:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM 'links' 
            '''
        )
        links = cursor.fetchall()
        return links
    
    def update_links_link(self, link_id: str):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            UPDATE 'links' SET link = 'https://teste02'
            WHERE id =? 
            ''', (link_id, )
        )

        self.__conn.commit()

    def delete_links(self, link_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            DELETE FROM links 
            WHERE id =? 
            ''', (link_id, )
        )
        self.__conn.commit()