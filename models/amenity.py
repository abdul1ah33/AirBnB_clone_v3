#!/usr/bin/python3
"""
Amenity Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

STORAGE_TYPE = os.environ.get('BTCPBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""
    __tablename__ = 'amenities'

    if STORAGE_TYPE == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship('PlaceAmenity',
                                       backref='amenities',
                                       cascade='delete')
    else:
        name = ''
