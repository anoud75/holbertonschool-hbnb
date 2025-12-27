#!/usr/bin/python3
"""Place model module"""

class Place:
    """Place class for accommodation listings"""
    
    def __init__(self, *args, **kwargs):
        """Initialize Place instance"""
        self.id = ""
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        
        # Update with any kwargs provided
        for key, value in kwargs.items():
            setattr(self, key, value)
