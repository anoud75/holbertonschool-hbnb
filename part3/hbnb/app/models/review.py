from app.models.base import BaseModel
from app.extensions import db
from sqlalchemy.orm import validates, relationship

class Review(BaseModel):
    """
    Represents a Review in the HBnB application.
    """
    __tablename__ = 'reviews'

    text = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.String(60), db.ForeignKey('places.id'), nullable=False)

    user = db.relationship('User', back_populates='reviews')
    place = db.relationship('Place', back_populates='reviews')

    @validates('text')
    def validate_text(self, key, value):
        if not value or value.strip() == "":
            raise ValueError("Review text cannot be empty")
        return value

    @validates('rating')
    def validate_rating(self, key, value):
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        return value