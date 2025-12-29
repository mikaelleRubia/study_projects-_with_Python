from flask import jsonify, Blueprint, request
from src.controller.link_creator import LinkCreator
from src.controller.link_finder import LinkFinder
from src.controller.trip_confirmer import TripConfirmer
from src.controller.trip_creator import TripCreator
from src.controller.trip_finder import TripFinder
from src.main.models.repositories.links_repository import LinkRepository
from src.main.models.repositories.trips_repository import TripsRepository
from src.main.models.repositories.emails_to_invite_repository import EmailToInviteRepository
from src.main.models.settings.db_connection_handler import db_connection_handler


trips_routes_bp = Blueprint("trip_routes", __name__)

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_to_invites_repository = EmailToInviteRepository(conn)
    controller = TripCreator(trips_repository, emails_to_invites_repository)
    
    response, status_code = controller.create(request.json)
    
    return jsonify(response), status_code

@trips_routes_bp.route("/trips/<trip_id>", methods=["GET"])
def find_trip_details(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    controller = TripFinder(trips_repository)
    
    response, status_code = controller.find_trip_details(trip_id)
    
    return jsonify(response), status_code


@trips_routes_bp.route("/trips/<trip_id>/confirm", methods=["GET"])
def trip_confirmer(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    controller = TripConfirmer(trips_repository)
    
    response, status_code = controller.confirmer(trip_id)
    
    return jsonify(response), status_code

@trips_routes_bp.route("/trips/<trip_id>/links", methods=["POST"])
def create_trip_link(trip_id):
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)

    controller = LinkCreator(link_repository)
    
    response, status_code = controller.create(request.json, trip_id)
    
    return jsonify(response), status_code


@trips_routes_bp.route("/trips/<trip_id>/all", methods=["GET"])
def find_trip_link(trip_id):
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)

    controller = LinkFinder(link_repository)
    
    response, status_code = controller.find(trip_id)
    
    return jsonify(response), status_code