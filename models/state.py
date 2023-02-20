#!/usr/bin/python3
"""
Module provides Class State
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class, inherits from BaseModel
    """

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)