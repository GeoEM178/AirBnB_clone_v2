#!/usr/bin/python3
""" State Module for HBNB project """

from os import environ
import models
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    se = environ.get("HBNB_TYPE_STORAGE")
    if (se == 'db'):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """cities function"""
            cities = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cities.append(value)
            return cities
