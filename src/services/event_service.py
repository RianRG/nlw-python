import uuid

from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.error_types.http_not_found import HttpNotFoundError

class EventsService:
  def __init__(self):
    self.__eventsRepository = EventsRepository()

  def add(self, request: HttpRequest) -> HttpResponse:

    body = request.body
    body["uuid"] = str(uuid.uuid4())

    self.__eventsRepository.addEvent(body)
    return HttpResponse(
      body={ "id": body["uuid"] },
      statusCode=201
    )

  def getById(self, request: HttpRequest) -> HttpResponse:
    eventId = request.params["eventId"]
    event = self.__eventsRepository.getEventById(eventId)

    if not event: raise HttpNotFoundError('Event not found!')

    eventAttendeesCount = self.__eventsRepository.countEventAttendees(eventId)

    return HttpResponse(
      body={
        "event": {
          "id": event.id,
          "title": event.title,
          "details": event.details,
          "slug": event.slug,
          "maximumAttendees": event.maximumAttendees,
          "attendeesAmount": eventAttendeesCount
        }
      },
      statusCode=200
    )
