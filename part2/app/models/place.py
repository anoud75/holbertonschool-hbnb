#!/usr/bin/python3
"""This module defines the Place class."""
from app.models.base_model import BaseModel


class Place(BaseModel):
    """Class representing a place."""

    def __init__(self, title, description, price, latitude, longitude, owner):
        """Initialize a new Place instance."""
        super().__init__()
        self.title = None
        self.description = description or ""
        self.price = None
        self.latitude = None
        self.longitude = None
        self.owner = owner
        self.owner_id = owner.id
        self.reviews = []
        self.amenities = []

        self.set_title(title)
        self.set_price(price)
        self.set_latitude(latitude)
        self.set_longitude(longitude)

        owner.add_place(self)

    def set_title(self, title):
        """Set and validate place title."""
        if not title or len(title) > 100:
            raise ValueError("Title must be between 1 and 100 characters")
        self.title = title

    def set_price(self, price):
        """Set and validate price."""
        if price is None or price < 0:
            raise ValueError("Price must be a positive value")
        self.price = float(price)

    def set_latitude(self, latitude):
        """Set and validate latitude."""
        if latitude is None or latitude < -90.0 or latitude > 90.0:
            raise ValueError("Latitude must be between -90.0 and 90.0")
        self.latitude = float(latitude)

    def set_longitude(self, longitude):
        """Set and validate longitude."""
        if longitude is None or longitude < -180.0 or longitude > 180.0:
            raise ValueError("Longitude must be between -180.0 and 180.0")
        self.longitude = float(longitude)

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def to_dict(self):
        """Return a dictionary representation of the place."""
        result = super().to_dict()
        result.pop('owner', None)
        result.pop('reviews', None)
        result['amenities'] = [a.id for a in self.amenities]
        return result
