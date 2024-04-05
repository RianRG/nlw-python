from typing import Dict
from src.models.settings.connection import dbConnectionHandler
from src.models.entities.attendees import Attendees
from src.models.entities.events import Events

class AttendeesRepository:
  def addAttendee(self, data: Dict) -> Dict:
    with dbConnectionHandler as database:
      attendee = Attendees(
        id = data.get("uuid"),
        name = data.get("name"),
        email = data.get("email"),
        eventId = data.get("eventId"),
        createdAt = data.get("createdAt")
      )
      database.session.add(attendee)
      database.session.commit()
      return data
  
  def getAttendeeBadgeById(self, attendeeId) -> Attendees:
    with dbConnectionHandler as database:
      attendee = (
        database.session.
        query(Attendees)
        .join(Events, Events.id == Attendees.eventId)
        .filter(Attendees.id == attendeeId)
        .with_entities(
          Attendees.name,
          Attendees.email,
          Events.title
        )
        .one()
      )
      return attendee