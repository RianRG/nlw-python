from src.models.settings.connection import dbConnectionHandler
from typing import Dict
from src.models.entities.events import Events

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