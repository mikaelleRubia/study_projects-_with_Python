from flask import jsonify, Blueprint, request
from src.controller.participant_confirmer import ParticipantConfirmer
from src.controller.participant_creator import ParticipantCreator
from src.controller.participant_finder import ParticipantFinder
from src.main.models.repositories.participants_repository import ParticipantsRepository
from src.main.models.settings.db_connection_handler import db_connection_handler


participants_routes_bp = Blueprint("participant_routes", __name__)

@participants_routes_bp.route("/participant", methods=["POST"])
def create_participant():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantCreator(participants_repository)
    
    response, status_code = controller.create(request.json)
    
    return jsonify(response), status_code

@participants_routes_bp.route("/participants", methods=["GET"])
def find_participant_all():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantFinder(participants_repository)
    
    response, status_code = controller.finds_all()
    
    return jsonify(response), status_code


@participants_routes_bp.route("/participants/<participant_id>", methods=["GET"])
def find_participant_details(participant_id):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantFinder(participants_repository)

    
    response, status_code = controller.find(participant_id)
    
    return jsonify(response), status_code


@participants_routes_bp.route("/participants/<participant_id>/confirm", methods=["GET"])
def participant_confirmer(participant_id):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    controller = ParticipantConfirmer(participants_repository)
    
    response, status_code = controller.confirmer(participant_id)
    
    return jsonify(response), status_code
