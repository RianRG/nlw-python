from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.event_handler import EventHandler

eventRouteBp = Blueprint("event_route", __name__)

@eventRouteBp.route("/events", methods=["POST"])
def createEvent():

  print(f"KKK:::::::::::::::::::::::::::: { request.get_json() }")
  
  httpRequest = HttpRequest(body=request.get_json())
  eventHandler = EventHandler()

  httpResponse = eventHandler.addEvent(httpRequest)
  return jsonify(httpResponse.body), httpResponse.statusCode