from sqlite3 import Connection
from typing import Dict, List, Tuple

class ParticipantsRepository:
    def __init__(self, conn: Connection) -> None:
            if conn is None:
                raise Exception("Conexão com o banco de dados não pode ser None")
            self.__conn = conn


    def create_participant(self, participant: Dict):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO participants 
                (id, trip_id, emails_to_invite_id, name, is_confirmed )
            VALUES (?, ?, ?, ?, ?)
            ''',(participant["id"], 
                participant["trip_id"], 
                participant["emails_to_invite_id"], 
                participant["name"], 
                0
            )
            
        )
        self.__conn.commit()

    def find_participant(self, participant_id: str)-> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM 'participants' WHERE id =? 
            ''', (participant_id, )
        )
        participant = cursor.fetchone()
        return participant
    
    def find_trip_id_participant(self, trip_id: str)-> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM 'participants' WHERE trip_id =? 
            ''', (trip_id, )
        )
        participant = cursor.fetchall()
        return participant
    
    def find_participant_all(self)-> List:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM 'participants' 
            '''
        )
        participant = cursor.fetchall()
        return participant
    
    def update_participant_is_confirmed(self, participant_id: str):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            UPDATE 'participants' SET is_confirmed = 1
            WHERE id =? 
            ''', (participant_id, )
        )

        self.__conn.commit()

    def delete_participant(self, participant_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            DELETE FROM participants
            WHERE id =? 
            ''', (participant_id, )
        )
        self.__conn.commit()