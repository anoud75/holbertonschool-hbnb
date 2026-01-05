#!/usr/bin/python3
"""This module defines the BaseModel class."""
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models with common attributes."""

    def __init__(self):
        """Initialize a new BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp."""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update attributes from a dictionary."""
        for key, value in data.items():
            if hasattr(self, key) and key not in ['id', 'created_at', 'updated_at']:
                setattr(self, key, value)
        self.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        result = self.__dict__.copy()
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
