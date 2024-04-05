import uuid

from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.error_types.http_not_found import HttpNotFoundError
from src.errors.error_types.http_conflict import HttpConflictError

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
    ): raise HttpConflictError('Max capacity reached!')

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

    if not badge: raise HttpNotFoundError('Attendee not found!')

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
  
  def getByEventId(self, req: HttpRequest) -> HttpResponse:
    eventId = req.params["eventId"]
    attendees = self.__attendeesRepository.getAttendeesByEventId(eventId)

    if not attendees: raise HttpNotFoundError('There are no attendees here!')

    formattedAttendees = []

    for attendee in attendees:
      formattedAttendees.append({
        "id": attendee.id,
        "name": attendee.name,
        "email": attendee.email,
        "checkedAt": attendee.checkedInAt,
        "createdAt": attendee.createdAt
      })

    return HttpResponse(
      body={
        "attendees": formattedAttendees
      },
      statusCode=200
    )




