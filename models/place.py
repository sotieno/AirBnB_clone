#!/usr/bin/python3
"""
Module provides Class Place
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class, inherits from BaseModel
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitiude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
