from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from utilities.db import Base

class Mixer(Base):
    __tablename__ = "mixers_table"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user_table.id"))
    name = Column(String, nullable=False)
    volume = Column(Integer, nullable=False)

    user = relationship("User", back_populates="mixers")
