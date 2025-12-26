import pytest
import uuid
from src.main.models.repositories.emails_to_invite_repository import EmailToInviteRepository
from src.main.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

@pytest.mark.skip(reason="interação com o banco")
def test_create_emails_to_invite():
    conn = db_connection_handler.get_connection()
    emails_to_invites_repository = EmailToInviteRepository(conn)

    emails_to_invites_infos ={
        "id": str(uuid.uuid4()),
        "trip_id": "2deb947c-1905-408b-afc5-f760f83c8838",
        "email":"email de teste"

    }
    emails_to_invites_repository.create_emails_to_invite(emails_to_invites_infos)
    

def test_find_emails_to_invite():
    conn = db_connection_handler.get_connection()
    emails_to_invites_repository = EmailToInviteRepository(conn)

    emails_to_invite_id = 'b05153e7-090c-4102-b711-d60e6e2a248d'
    emails_to_invite = emails_to_invites_repository.find_emails_to_invite(emails_to_invite_id)

    assert emails_to_invite is not None
    assert emails_to_invite[2] == "email de teste"


@pytest.mark.skip(reason="interação com o banco")
def test_update_emails_to_invite():
    conn = db_connection_handler.get_connection()
    emails_to_invites_repository = EmailToInviteRepository(conn)

    emails_to_invite_id = '9828720d-9fd8-468f-845a-2f69d553b973'
    emails_to_invites_repository.update_emails_to_invite_email(emails_to_invite_id)
    emails_to_invite = emails_to_invites_repository.find_emails_to_invite(emails_to_invite_id)
    assert  emails_to_invite is not None
    assert emails_to_invite[2] == "EMAIL COM AJUSTE NO CORPO DE MENSAGEM" 


@pytest.mark.skip(reason="interação com o banco")
def test_delete_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invites_repository = EmailToInviteRepository(conn)

    emails_to_invite_id = 'ce5588fd-ec58-4ea7-a7c6-d51283f3d9fa'
    emails_to_invites_repository.delete_emails_to_invite(emails_to_invite_id)

    emails_to_invite_after_delete = emails_to_invites_repository.find_emails_to_invite(emails_to_invite_id)

    assert emails_to_invite_after_delete is None