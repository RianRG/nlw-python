from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.services.event_service import EventsService

eventRouteBp = Blueprint("event_route", __name__)

@eventRouteBp.route("/events", methods=["POST"])
def createEvent():

  httpRequest = HttpRequest(body=request.get_json())
  eventsService = EventsService()
  httpResponse = eventsService.add(httpRequest)

  return jsonify(httpResponse.body), httpResponse.statusCode

@eventRouteBp.route("/events/<eventId>", methods=["GET"])
def getEvent(eventId: str):
  httpRequest = HttpRequest(params={ "eventId": eventId })
  eventsService = EventsService()
  httpResponse = eventsService.getById(httpRequest)

  return jsonify(httpResponse.body), httpResponse.statusCode