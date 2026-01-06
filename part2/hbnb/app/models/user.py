#!/usr/bin/python3
"""User model."""
import re
import uuid
from datetime import datetime


class User:
    """User class."""

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.places = []
        self.reviews = []

    def update(self, data):
        """Update user attributes."""
        for key, value in data.items():
            if key not in ['id', 'created_at']:
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert to dictionary."""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
