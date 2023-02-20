#!/usr/bin/python3
"""
Module provides Class Amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class, inherits from BaseModel
    """

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
