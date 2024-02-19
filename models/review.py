#!/usr/bin/python3
""" Review module for the HBNB project """

from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from models.place import Place
from models.user import User


class Review(BaseModel):
    """ Review classto store review information """
    se = environ.get("HBNB_TYPE_STORAGE")
    if (se == 'db'):
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey("places.id"))
        user_id = Column(String(60), ForeignKey("users.id"))
        text = Column(String(1024), nullable=False)
        place = relationship("Place", back_populates="reviews")
    else:
        place_id = ""
        user_id = ""
        text = ""
