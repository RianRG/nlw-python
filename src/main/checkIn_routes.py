from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.services.event_service import EventsService
from src.services.checkin_service import CheckInService

checkInRouteBp = Blueprint("checkInRouteBp", __name__)

@checkInRouteBp.route("/attendees/<attendeeId>/check-in", methods=["POST"])
def checkInAttendee(attendeeId: str):
  checkInService = CheckInService()

  httpRequest = HttpRequest(params={ "attendeeId": attendeeId })

  httpResponse = checkInService.checkIn(httpRequest)

  return jsonify(httpResponse.body), httpResponse.statusCode
