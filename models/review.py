#!/usr/bin/python3
"""Python module for Review class inherited from BaseModel class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class."""
    place_id = ""
    user_id = ""
    text = ""
