from .events_repository import EventsRepository
from src.models.settings.connection import dbConnectionHandler

dbConnectionHandler.connectDb()

# def test_addEvent():

#   event = {
#     "uuid": "my-id-1-3",
#     "title": "event",
#     "slug": "event-02",
#     "maximumAttendees": 50
#   }

#   eventsRepository = EventsRepository()
#   print(eventsRepository.addEvent(event))

def test_getEventById():
  eventsRepository = EventsRepository()
  print(eventsRepository.getEventById("my-id-1-3"))

def test_getEvents():
  eventsRepository = EventsRepository()
  print(f"ajakjkasajsa:::: {eventsRepository.getEvents()}")
    