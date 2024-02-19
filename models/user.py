#!/usr/bin/python3
"""This module defines a class User"""
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    se = os.getenv('HBNB_TYPE_STORAGE') == 'db'
    if (se == 'db'):
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
