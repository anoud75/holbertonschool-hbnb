from app.extensions import db
import uuid
from datetime import datetime

class BaseModel(db.Model):
    """
    Base class for all models in the HBnB application.

    This class provides a set of common attributes and methods that are shared
    across all entities, such as unique identification (UUID) and timestamp management
    (created_at, updated_at).
    """
    __abstract__ = True
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary
        Args:
            data (dict): A dictionary where keys match the attribute names 
            and values are the new values to set.
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save() 