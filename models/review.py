#!/bin/bash/python3
"""Review module"""
from models.base_model import BaseModel

class Review(BaseModel):
    """class Review that inherits from base """

    place_id = ""
    user_id = ""
    text = ""
