#!/usr/bin/pythone
"""Defines the Place class that inherits from BaseModel"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Represents user reviews"""
    place_id = ""
    user_id = ""
    text = ""
