 
from app.models.base import BaseModel

class Amenity(BaseModel):
    """
    Represents an Amenity in the HBnB application.

    Amenities are features associated with a Place, such as 'Wi-Fi', 'Swimming Pool',
    or 'Air Conditioning'. This class inherits from BaseModel to gain standard
    attributes like unique ID, creation timestamp, and update timestamp.
    """
    def __init__(self, name):
        """
        Initialize a new Amenity.

        Args:
            name (str): The name of the amenity (e.g., "Wi-Fi").

        Raises:
            ValueError: If the amenity name exceeds 50 characters.
        """
        super().__init__()
        self.name = name

        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters")
