from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from utilities.db import Base

class Food(Base):
    __tablename__ = "food_table"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user_table.id"))
    type = Column(String)  # vegetarian, non-vegetarian
    name = Column(String, nullable=False)
    servings = Column(Integer, nullable=False)

    user = relationship("User", back_populates="foods")
