from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

class CheckIns(Base):
  __tablename__ = "checkIns"

  id = Column(String, primary_key=True)
  createdAt = Column(DateTime, default=func.now())
  attendeeId = Column(String, ForeignKey("attendees.id"))