from src.models.settings.connection import dbConnectionHandler
from typing import Dict
from src.models.entities.events import Events
import json

class EventsRepository:
  def addEvent(self, data: Dict) -> Dict:
    with dbConnectionHandler as database:
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
  
  def getEventById(self, eventId: str) -> Dict:
    with dbConnectionHandler as database:
      response = database.session.query(Events).filter(Events.id==eventId).one()

      return response

  def getEvents(self):
    with dbConnectionHandler as database:
      response = database.session.query(Events)
      return response