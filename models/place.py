#!/usr/bin/python3
""" Place Module for HBNB project """
from os import environ
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Float, Integer, Table, ForeignKey


class Place(BaseModel):
    """ A place to stay """
    se = os.getenv('HBNB_TYPE_STORAGE') == 'db'

    if se == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))
    __tablename__ = "places"
    if (se == "db"):
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        amenities = relationship("Amenity", back_populates="place_amenities",
                                 secondary=place_amenity, viewonly=False)
        reviews = relationship("Review", back_populates="place")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """getter of amenity"""
            amenitie = []
            queryRes = models.dummy_classes['Amenity']
            for j in models.storage.all(queryRes).values():
                if j in self.amenity_ids:
                    amenitie.append(j)
            return amenitie

        @amenities.setter
        def amenities(self, obj):
            """setter pf amentitees"""
            if type(obj) is Amenity:
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)

        @property
        def reviews(self):
            """getter of reviews"""
            review = []
            queryRes = models.dummy_classes['Review']
            for i in models.storage.all(queryRes).values():
                if i.place_id == self.id:
                    review.append(i)
            return review
