#!/bin/bash/python3
"User module"""
from models.base_model import BaseModel

class User(BaseModel):
    """class User that inherits from base"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
