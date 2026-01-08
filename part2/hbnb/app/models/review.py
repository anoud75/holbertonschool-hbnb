 
from app.models.base import BaseModel

class Review(BaseModel):
    """
    Represents a Review in the HBnB application.

    A Review consists of a text body and a rating (1-5), written by a User
    for a specific Place. It inherits unique ID and timestamping functionalities
    from the BaseModel class.
    """
    def __init__(self, text, rating, place, user):
        """
        Initialize a new Review.

        Args:
            text (str): The content of the review. Cannot be empty.
            rating (int): The numeric rating, must be an integer between 1 and 5.
            place (Place): The Place object that is being reviewed.
            user (User): The User object who wrote the review.

        Raises:
            ValueError: If validation for text or rating fails during initialization.
        """
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
        
    @property
    def text(self):
        """Get the text content of the review."""
        return self._text

    @text.setter
    def text(self, value):
        """
        Set the review text with validation.

        Raises:
            ValueError: If the text is None, empty, or contains only whitespace.
        """
        if not value or value.strip() == "":
            raise ValueError("Review text cannot be empty")
        self._text = value

    @property
    def rating(self):
        """Get the numeric rating of the review."""
        return self._rating

    @rating.setter
    def rating(self, value):
        """
        Set the rating with validation.

        Args:
            value (int): The rating value.

        Raises:
            ValueError: If the value is not an integer or is not between 1 and 5.
        """
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        self._rating = value