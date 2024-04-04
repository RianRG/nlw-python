import uuid

from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class AttendeeService:
  def __init__(self):
    self.__attendeesRepository = AttendeesRepository()
    self.__eventsRepository = EventsRepository()

  def add(self, request: HttpRequest) -> HttpResponse:
    body = request.body
    eventId = request.params["eventId"]
    print(f"EVENTID::::: {eventId}")

    eventAttendeesCount = self.__eventsRepository.countEventAttendees(eventId)
    print(f"KKKK::::::::::::::::::: {eventAttendeesCount}")
    if(
      eventAttendeesCount["attendeesAmount"] and 
      eventAttendeesCount["maximumAttendees"] <= eventAttendeesCount["attendeesAmount"]
    ): raise Exception('Max capacity reached!')

    body["uuid"] = str(uuid.uuid4())

    body["eventId"] = eventId

    
    print(f"BODY::::: {body}")

    self.__attendeesRepository.addAttendee(body)

    return HttpResponse(
      body=None,
      statusCode=201
    )



