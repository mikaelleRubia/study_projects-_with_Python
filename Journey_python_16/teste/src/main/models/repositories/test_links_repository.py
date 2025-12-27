import pytest
import uuid
from src.main.models.repositories.links_repository import LinkRepository
from src.main.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

@pytest.mark.skip(reason="interação com o banco")
def test_create_links():
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)

    links_infos ={
        "id": str(uuid.uuid4()),
        "trip_id": "c9db5194-ca97-417b-a083-6629a54e6698",
        "link":"https://linkDeTeste",
        "title": "Titulo para teste"

    }
    link_repository.create_links(links_infos)
    

def test_find_links():
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)

    link_id = 'be3100b3-f36a-412e-a7d1-ce54480fd2ac'
    link = link_repository.find_links(link_id)

    assert link is not None
    assert link[3] == "Titulo para teste"


@pytest.mark.skip(reason="interação com o banco")
def test_update_links():
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)

    link_id = 'a8b879ec-5b18-433e-9782-828978e44a6f'
    link_repository.update_links_link(link_id)
    link = link_repository.find_links(link_id)
    assert  link is not None
    assert link[2] == "https://teste02" 


@pytest.mark.skip(reason="interação com o banco")
def test_delete_trip():
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)

    link_id = '95b42308-bbc9-4b18-9da5-492b03b0d507'
    link_repository.delete_links(link_id)

    link_after_delete = link_repository.find_links(link_id)

    assert link_after_delete is None