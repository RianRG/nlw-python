from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.services.event_service import EventsService
from src.errors.errors_service import ErrorsService

eventRouteBp = Blueprint("event_route", __name__)

@eventRouteBp.route("/events", methods=["POST"])
def createEvent():

  try:
    httpRequest = HttpRequest(body=request.get_json())
    eventsService = EventsService()
    httpResponse = eventsService.add(httpRequest)

    return jsonify(httpResponse.body), httpResponse.statusCode
  except Exception as exception:
    httpResponse = ErrorsService(exception)
    return jsonify(httpResponse.body), httpResponse.statusCode

@eventRouteBp.route("/events/<eventId>", methods=["GET"])
def getEvent(eventId: str):
  try:
    httpRequest = HttpRequest(params={ "eventId": eventId })
    eventsService = EventsService()
    httpResponse = eventsService.getById(httpRequest)

    return jsonify(httpResponse.body), httpResponse.statusCode
  except Exception as exception:
    httpResponse = ErrorsService(exception)
    return jsonify(httpResponse.body), httpResponse.statusCode