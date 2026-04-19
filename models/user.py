from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from utilities.db import Base

class User(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    rsvp = relationship("RSVP", back_populates="user", uselist=False, cascade="all, delete-orphan")
    foods = relationship("Food", back_populates="user", cascade="all, delete-orphan")
    liquors = relationship("Liquor", back_populates="user", cascade="all, delete-orphan")
    mixers = relationship("Mixer", back_populates="user", cascade="all, delete-orphan")
