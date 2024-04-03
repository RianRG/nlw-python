from src.models.settings.connection import dbConnectionHandler
from src.models.entities.checkIns import CheckIns

class CheckInsRepository:
  def addCheckIn(self, attendeeId):
    with dbConnectionHandler as database:

      checkIn = CheckIns(attendeeId=attendeeId)

      database.session.add(checkIn)
      database.session.commit()
      return attendeeId