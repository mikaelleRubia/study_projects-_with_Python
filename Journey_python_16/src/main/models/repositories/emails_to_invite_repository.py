from sqlite3 import Connection
from typing import Dict, Tuple

class EmailToInviteRepository:
    def __init__(self, conn: Connection )-> None:
        self.__conn = conn

    def create_emails_to_invite(self, emails_to_invite: Dict):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO emails_to_invite 
                (id, trip_id, email)
            VALUES (?, ?, ?)
            ''',(emails_to_invite["id"], 
               emails_to_invite["trip_id"], 
                emails_to_invite["email"], 
            )
        )
        self.__conn.commit()

    def find_emails_to_invite(self, emails_to_invite_id: str)-> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM 'emails_to_invite' WHERE id =? 
            ''', (emails_to_invite_id, )
        )
        trip = cursor.fetchone()
        return trip
    
    def update_emails_to_invite_email(self, emails_to_invite_id: str):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            UPDATE 'emails_to_invite' SET email = 'EMAIL COM AJUSTE NO CORPO DE MENSAGEM'
            WHERE id =? 
            ''', (emails_to_invite_id, )
        )

        self.__conn.commit()

    def delete_emails_to_invite(self, emails_to_invite_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            DELETE FROM emails_to_invite 
            WHERE id =? 
            ''', (emails_to_invite_id, )
        )
        self.__conn.commit()