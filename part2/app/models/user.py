#!/usr/bin/python3
"""This module defines the User class."""
import re
from app.models.base_model import BaseModel


class User(BaseModel):
    """Class representing a user."""

    def __init__(self, first_name, last_name, email, is_admin=False):
        """Initialize a new User instance."""
        super().__init__()
        self.first_name = None
        self.last_name = None
        self.email = None
        self.is_admin = is_admin
        self.places = []
        self.reviews = []

        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)

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

    def add_place(self, place):
        """Add a place to the user's list of places."""
        self.places.append(place)

    def add_review(self, review):
        """Add a review to the user's list of reviews."""
        self.reviews.append(review)

    def to_dict(self):
        """Return a dictionary representation of the user."""
        result = super().to_dict()
        result.pop('places', None)
        result.pop('reviews', None)
        return result
