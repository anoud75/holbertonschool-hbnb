from app.models.base import BaseModel
from app.extensions import db
from sqlalchemy.orm import validates, relationship

place_amenity = db.Table('place_amenity',
    db.Column('place_id', db.String(36), db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.String(36), db.ForeignKey('amenities.id'), primary_key=True)
)

class Place(BaseModel):
    """
    Represents a Place in the HBnB application.
    """
    __tablename__ = 'places'
    
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)

    owner = db.relationship('User', back_populates='places')
    reviews = db.relationship('Review', back_populates='place', cascade='all, delete-orphan')
    amenities = db.relationship('Amenity', secondary=place_amenity, back_populates='places')

    @validates('title')
    def validate_title(self, key, value):
        if len(value) > 100:
            raise ValueError("Title must be less than 100 characters")
        return value

    @validates('price')
    def validate_price(self, key, value):
        if value < 0:
            raise ValueError("Price should be a positive number")
        return value
    
    @validates('latitude')
    def validate_latitude(self, key, value):
        if not (-90.0 <= value <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0")
        return value

    @validates('longitude')
    def validate_longitude(self, key, value):
        if not (-180.0 <= value <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0")
        return value


    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)