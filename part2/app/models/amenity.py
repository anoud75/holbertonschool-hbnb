#!/usr/bin/python3
"""This module defines the Amenity class."""
from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing an amenity."""

    def __init__(self, name):
        """Initialize a new Amenity instance."""
        super().__init__()
        self.name = None
        self.set_name(name)

    def set_name(self, name):
        """Set and validate amenity name."""
        if not name or len(name) > 50:
            raise ValueError("Amenity name must be between 1 and 50 characters")
        self.name = name
