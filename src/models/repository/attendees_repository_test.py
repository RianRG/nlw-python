from src.models.settings.connection import dbConnectionHandler
from src.models.repository.attendees_repository import AttendeesRepository

dbConnectionHandler.connectDb()

def test_addAttendee():
  attendeesRepository = AttendeesRepository()

  print(attendeesRepository.addAttendee(
    data={
      "uuid": "111",
      "name": "Carlinhos",
      "email": "a@a.com",
      "eventId": "my-id-1-3"
    }
  ))

def test_getAttendeeBageById():
  attendeesRepository = AttendeesRepository()

  print(attendeesRepository.getAttendeeBadgeById("111"))