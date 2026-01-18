 
from app.models.base import BaseModel

class Place(BaseModel):
    """
    Represents a Place in the HBnB application.

    This class holds details about a property listing, including its location,
    pricing, owner, and associated reviews/amenities. It inherits validation logic
    and timestamping from BaseModel.
    """
    def __init__(self, title, description, price, latitude, longitude, owner):
        """
        Initialize a new Place.

        Args:
            title (str): The name of the listing (max 100 chars).
            description (str): A detailed text description of the place.
            price (float): The cost per night (must be positive).
            latitude (float): Geographic latitude (-90.0 to 90.0).
            longitude (float): Geographic longitude (-180.0 to 180.0).
            owner (User): The User object representing the host/owner.
        """
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

    @property
    def title(self):
        """Get the title of the place."""
        return self._title
    
    @title.setter
    def title(self, value):
        """
        Set the title with validation.
        
        Raises:
            ValueError: If the title exceeds 100 characters.
        """
        if len(value) > 100:
            raise ValueError("Title must be less than 100 characters")
        self._title = value


    @property
    def price(self):
        """Get the price per night."""
        return self._price
    
    @price.setter
    def price(self, value):
        """
        Set the price with validation.

        Raises:
            ValueError: If the price is negative.
        """
        if value < 0:
            raise ValueError("price should be a positive number")
        self._price = value
    
    @property
    def latitude(self):
        """Get the latitude coordinate."""
        return self._latitude
    
    @latitude.setter
    def latitude(self, value):
        """
        Set the latitude with validation.

        Raises:
            ValueError: If latitude is not between -90.0 and 90.0.
        """
        if not (-90.0 <= value <=90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0")
        self._latitude = value

    @property
    def longitude(self):
        """Get the longitude coordinate."""
        return self._longitude
    
    @longitude.setter
    def longitude(self, value):
        """
        Set the longitude with validation.

        Raises:
            ValueError: If longitude is not between -180.0 and 180.0.
        """
        if not (-180.0 <= value <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0")
        self._longitude = value

    def add_review(self, review):
        """Add a review to the place.
        Args:
            review (Review): The review instance to add.
        """
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place.
        Args:
            amenity (Amenity): The amenity instance to add.
        """
        self.amenities.append(amenity)
