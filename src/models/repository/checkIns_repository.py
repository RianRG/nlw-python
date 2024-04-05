from src.models.settings.connection import dbConnectionHandler
from src.models.entities.checkIns import CheckIns
from typing import Dict

class CheckInsRepository:
  def addCheckIn(self, attendeeId: str):
    with dbConnectionHandler as database:

      checkIn = CheckIns(attendeeId=attendeeId)

      database.session.add(checkIn)
      database.session.commit()
      return attendeeId