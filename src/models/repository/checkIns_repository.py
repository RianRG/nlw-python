from src.models.settings.connection import dbConnectionHandler
from src.models.entities.checkIns import CheckIns
from src.errors.error_types.http_conflict import HttpConflictError


class CheckInsRepository:
  def addCheckIn(self, attendeeId: str):
    with dbConnectionHandler as database:
      try:
        checkIn = CheckIns(attendeeId=attendeeId)

        database.session.add(checkIn)
        database.session.commit()
        return attendeeId
      except:
        raise HttpConflictError('Checkin already registered!')