from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

class Attendees(Base):
  __tablename__ = "attendees"

  id = Column(String, primary_key=True)
  name = Column(String, nullable=False)
  email = Column(String, nullable=False)
  eventId = Column(String, ForeignKey("events.id"))
  createdAt = Column(DateTime, default=func.now())