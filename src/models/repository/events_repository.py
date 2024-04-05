from src.models.settings.connection import dbConnectionHandler
from typing import Dict
from src.models.entities.events import Events
from src.models.entities.attendees import Attendees
from src.errors.error_types.http_conflict import HttpConflictError

class EventsRepository:
  def addEvent(self, data: Dict) -> Dict:
      with dbConnectionHandler as database:
        try:
          event = Events(
            id=data.get("uuid"),
            title=data.get("title"),
            details=data.get("details"),
            slug=data.get("slug"),
            maximumAttendees=data.get("maximumAttendees")
          )

          database.session.add(event)
          database.session.commit()
          return data
        except: 
          raise HttpConflictError('Event already registered!')

  
  def getEventById(self, eventId: str) -> Dict:
    with dbConnectionHandler as database:
      response = database.session.query(Events).filter(Events.id==eventId).one()

      return response

  def countEventAttendees(self, eventId: str) -> Dict:
    with dbConnectionHandler as database:
      response = (
        database.session
        .query(Events)
        .join(Attendees, Events.id == Attendees.eventId)
        .filter(Events.id == eventId)
        .with_entities(
          Events.maximumAttendees,
          Attendees.id
        )
        .all()
      )

      if len(response)==0:
        return{
          "attendeesAmount": 0
        }
      return {
        "maximumAttendees": response[0].maximumAttendees,
        "attendeesAmount": len(response)
      }