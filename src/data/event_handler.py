import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventHandler:
  def __init__(self):
    self.__eventsRepository = EventsRepository()

  def addEvent(self, request: HttpRequest) -> HttpResponse:
    body = request.body
    body["uuid"] = str(uuid.uuid4())
    self.__eventsRepository.addEvent(body)

    return HttpResponse(
      body={ "id": body["uuid"] },
      statusCode=201
    )