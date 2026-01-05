#!/usr/bin/python3
"""This module defines the Review class."""
from app.models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a review."""

    def __init__(self, text, rating, place, user):
        """Initialize a new Review instance."""
        super().__init__()
        self.text = None
        self.rating = None
        self.place = place
        self.place_id = place.id
        self.user = user
        self.user_id = user.id

        self.set_text(text)
        self.set_rating(rating)

        if place.owner_id == user.id:
            raise ValueError("Owner cannot review their own place")

        place.add_review(self)
        user.add_review(self)

    def set_text(self, text):
        """Set and validate review text."""
        if not text:
            raise ValueError("Review text is required")
        self.text = text

    def set_rating(self, rating):
        """Set and validate rating."""
        if rating is None or rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        self.rating = int(rating)

    def to_dict(self):
        """Return a dictionary representation of the review."""
        result = super().to_dict()
        result.pop('place', None)
        result.pop('user', None)
        return result
