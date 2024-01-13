#!/usr/bin/python3
"""
Creating a review class that inherits form BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class has public attributes
    """
    place_id = ""
    user_id = ""
    text = ""


def __init__(self, *args, **kwargs):
    """
    init
    """
    super().__init__(*args, **kwargs)
