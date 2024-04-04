from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.services.attendee_service import AttendeeService

attendeeRouteBp = Blueprint("attendee_route", __name__)

@attendeeRouteBp.route('/events/<eventId>/register', methods=["POST"])
def createAttendee(eventId: str):
  httpRequest = HttpRequest(body=request.get_json(), params={ "eventId": eventId })
  attendeeService = AttendeeService()

  httpResponse = attendeeService.add(httpRequest)

  return jsonify(httpResponse.body), httpResponse.statusCode

