from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from utilities.db import Base

class Liquor(Base):
    __tablename__ = "liqour_table"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user_table.id"))
    type = Column(String)  # from list of liquors
    brand = Column(String, nullable=False)
    variant = Column(String, default="Standard")
    volume = Column(Integer, nullable=False)

    user = relationship("User", back_populates="liquors")
