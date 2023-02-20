#!/usr/bin/python3
"""
Module provides Class User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class, inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
