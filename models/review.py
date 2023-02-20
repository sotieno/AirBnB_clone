#!/usr/bin/python3
"""
Module provides Class Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class, inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
