from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from utilities.db import Base

class RSVP(Base):
    __tablename__ = "rsvp_table"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user_table.id"), unique=True)
    status = Column(String)  # yes, no, tentative
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="rsvp")
    days = relationship("RSVPDay", back_populates="rsvp", cascade="all, delete-orphan")

class RSVPDay(Base):
    __tablename__ = "rsvp_day_table"

    id = Column(Integer, primary_key=True, index=True)
    rsvp_id = Column(Integer, ForeignKey("rsvp_table.id"))
    day_name = Column(String, nullable=False)

    rsvp = relationship("RSVP", back_populates="days")

