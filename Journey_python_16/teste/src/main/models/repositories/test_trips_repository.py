import pytest
import uuid
from datetime import datetime, timedelta
from src.main.models.repositories.trips_repository import TripsRepository
from src.main.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

@pytest.mark.skip(reason="interação com o banco")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_infos ={
        "id": str(uuid.uuid4()),
        "destination": "Osasco",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5), 
        "owner_name": "Admin",
        "owner_email":"admin@gmail.com"
    }
    trips_repository.create_trip(trips_infos)
    

def test_find_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trip_id = '2deb947c-1905-408b-afc5-f760f83c8838'
    trip = trips_repository.find_trip(trip_id)

    assert trip is not None
    assert trip[1] == "Osasco"


@pytest.mark.skip(reason="interação com o banco")
def test_update_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trip_id = '2deb947c-1905-408b-afc5-f760f83c8838'
    trips_repository.update_trip_status(trip_id)
    trip = trips_repository.find_trip(trip_id)
    assert trip is not None
    assert trip[6] == 1


@pytest.mark.skip(reason="interação com o banco")
def test_delete_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trip_id = '65a9cd28-3af9-476a-933a-44d25aa9f804'
    trips_repository.delete_trip(trip_id)

    trip_after_delete = trips_repository.find_trip(trip_id)

    assert trip_after_delete is None