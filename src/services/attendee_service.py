import uuid

from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class AttendeeService:
  def __init__(self):
    self.__attendeesRepository = AttendeesRepository()
    self.__eventsRepository = EventsRepository()

  def add(self, req: HttpRequest) -> HttpResponse:
    body = req.body
    eventId = req.params["eventId"]

    eventAttendeesCount = self.__eventsRepository.countEventAttendees(eventId)
    if(
      eventAttendeesCount["attendeesAmount"] and 
      eventAttendeesCount["maximumAttendees"] <= eventAttendeesCount["attendeesAmount"]
    ): raise Exception('Max capacity reached!')

    body["uuid"] = str(uuid.uuid4())

    body["eventId"] = eventId

    

    self.__attendeesRepository.addAttendee(body)

    return HttpResponse(
      body=None,
      statusCode=201
    )
  
  def getBadgeById(self, req: HttpRequest) -> HttpResponse:
    attendeeId = req.params["attendeeId"]

    badge = self.__attendeesRepository.getAttendeeBadgeById(attendeeId)

    if not badge: raise Exception('Attendee not found!')

    return HttpResponse(
      body={
        "badge": {
          "name": badge.name,
          "email": badge.email,
          "eventTitle": badge.title
        }
      },
      statusCode=200
    )




