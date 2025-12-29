import pytest
import uuid
from src.main.models.repositories.participants_repository import ParticipantsRepository
from src.main.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

@pytest.mark.skip(reason="interação com o banco")
def test_create_participants():
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    participant_infos ={
        "id": str(uuid.uuid4()),
        "trip_id": "22173463-a973-4dd0-97bd-f34803ae0a32",
        "emails_to_invite_id": "c3ec5889-55ba-4e0b-99d7-7577422959c5",
        "name": "Cris",

    }
    participant_repository.create_participant(participant_infos)
    

def test_find_participants_all():
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    participants = participant_repository.find_participant_all()

    assert isinstance(participants, list)


def test_find_participants():
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    participantid = 'f0a5a65c-b64b-4765-b478-9d8fb02f51de'
    participant = participant_repository.find_participant(participantid)

    assert participant is not None
    assert participant[3] == "Cris"


@pytest.mark.skip(reason="interação com o banco")
def test_update_participants():
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    participant_id = 'f0a5a65c-b64b-4765-b478-9d8fb02f51de'
    participant_repository.update_participant_is_confirmed(participant_id)
    participant = participant_repository.find_participant(participant_id)
    assert  participant is not None
    assert participant[4] == 1 


@pytest.mark.skip(reason="interação com o banco")
def test_delete_trip():
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    participant_id = '3e84e569-8334-44d0-9275-ae0bdcb93195'
    participant_repository.delete_participant(participant_id)

    participant_after_delete = participant_repository.find_participant(participant_id)

    assert participant_after_delete is None