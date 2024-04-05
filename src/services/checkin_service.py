from src.models.repository.checkIns_repository import CheckInsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
import uuid

class CheckInService:
  def __init__(self):
    self.__checkInsRepository = CheckInsRepository()

  def checkIn(self, req: HttpRequest) -> HttpResponse:
    attendeeId = req.params["attendeeId"]
    print(f"ATTENDEEID:::::::::: {attendeeId}")
    self.__checkInsRepository.addCheckIn(attendeeId)

    return HttpResponse(
      body=None,
      statusCode=201
    )