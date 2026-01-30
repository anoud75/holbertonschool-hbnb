from app.models.base import BaseModel
from app.extensions import db
from sqlalchemy.orm import validates

class Amenity(BaseModel):
    """
    Represents an Amenity in the HBnB application.
    """
    __tablename__ = 'amenities' # Changed from 'amenity' to match ForeignKey references
    
    name = db.Column(db.String(50), nullable=False, unique=True)
    

    places = db.relationship('Place', secondary='place_amenity', back_populates='amenities')

    @validates('name')
    def validate_name(self, key, value):
        if not isinstance(value, str): # FIXED: Was isinstance(self, key, value)
            raise TypeError("Name must be a string")
        if not value:
            raise TypeError("Name can't be empty")
        if len(value) > 50:
            raise ValueError("Name must be less than or equal to 50 char")
        return value