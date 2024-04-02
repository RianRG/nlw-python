from .events_repository import EventsRepository
from src.models.settings.connection import dbConnectionHandler

dbConnectionHandler.connectDb()

def test_addEvent():

  event = {
    "uuid": "my-id-1-2",
    "title": "event",
    "slug": "event-01",
    "maximumAttendees": 50
  }

  eventsRepository = EventsRepository()
  print(eventsRepository.addEvent(event))