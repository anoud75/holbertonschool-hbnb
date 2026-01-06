#!/usr/bin/python3
"""This module defines the User class."""
import re
import uuid
from datetime import datetime


class User:
    """Class representing a user."""

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        """Initialize a new User instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.first_name = None
        self.last_name = None
        self.email = None
        self.password = None
        self.is_admin = is_admin
        self.places = []
        self.reviews = []
        
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_password(password)

    def set_first_name(self, first_name):
        """Set and validate first name."""
        if not first_name or len(first_name) > 50:
            raise ValueError("First name must be between 1 and 50 characters")
        self.first_name = first_name

    def set_last_name(self, last_name):
        """Set and validate last name."""
        if not last_name or len(last_name) > 50:
            raise ValueError("Last name must be between 1 and 50 characters")
        self.last_name = last_name

    def set_email(self, email):
        """Set and validate email."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not email or not re.match(email_regex, email):
            raise ValueError("Invalid email format")
        self.email = email

    def set_password(self, password):
        """Set and validate password."""
        if not password or len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")
        self.password = password

    def add_place(self, place):
        """Add a place to the user's list of places."""
        self.places.append(place)

    def add_review(self, review):
        """Add a review to the user's list of reviews."""
        self.reviews.append(review)

    def update(self, data):
        """Update user attributes from a dictionary."""
        if 'first_name' in data:
            self.set_first_name(data['first_name'])
        if 'last_name' in data:
            self.set_last_name(data['last_name'])
        if 'email' in data:
            self.set_email(data['email'])
        if 'password' in data:
            self.set_password(data['password'])
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the user."""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,  # Will be removed in API responses
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        } 
