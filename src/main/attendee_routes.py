from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.services.attendee_service import AttendeeService
from src.errors.errors_service import ErrorsService


attendeeRouteBp = Blueprint("attendee_route", __name__)

@attendeeRouteBp.route('/events/<eventId>/register', methods=["POST"])
def createAttendee(eventId: str):
  try: 
    httpRequest = HttpRequest(body=request.get_json(), params={ "eventId": eventId })
    attendeeService = AttendeeService()

    httpResponse = attendeeService.add(httpRequest)

    return jsonify(httpResponse.body), httpResponse.statusCode
  except Exception as exception:
    httpResponse = ErrorsService(exception)
    return jsonify(httpResponse.body), httpResponse.statusCode

@attendeeRouteBp.route('/attendees/<attendeeId>/badge', methods=["GET"])
def getAttendeeBadge(attendeeId: str):
  try:
    httpRequest = HttpRequest(params={ "attendeeId": attendeeId })
    attendeeService = AttendeeService()

    httpResponse = attendeeService.getBadgeById(httpRequest)

    return jsonify(httpResponse.body), httpResponse.statusCode
  except Exception as exception:
    httpResponse = ErrorsService(exception)
    return jsonify(httpResponse.body), httpResponse.statusCode

@attendeeRouteBp.route('/events/<eventId>/attendees', methods=["GET"])
def getAttendeesFromEvent(eventId: str):
  try:
    httpRequest = HttpRequest(params={ "eventId": eventId })
    attendeeService = AttendeeService()

    httpResponse = attendeeService.getByEventId(httpRequest)

    return jsonify(httpResponse.body), httpResponse.statusCode
  except Exception as exception:
    httpResponse = ErrorsService(exception)
    return jsonify(httpResponse.body), httpResponse.statusCode