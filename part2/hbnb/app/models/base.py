import uuid
from datetime import datetime

class BaseModel:
    """
    Base class for all models in the HBnB application.

    This class provides a set of common attributes and methods that are shared
    across all entities, such as unique identification (UUID) and timestamp management
    (created_at, updated_at).
    """
    def __init__(self):
        """
        Initialize a new instance of BaseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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