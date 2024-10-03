# core/models/kitten.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.db import Base


class Kitten(Base):
    __tablename__ = "kittens"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    color = Column(String)
    age_in_months = Column(Integer)
    description = Column(String)
    breed_id = Column(Integer, ForeignKey("breeds.id"), nullable=False)
    breed = relationship("Breed", back_populates="kittens", lazy="joined")
