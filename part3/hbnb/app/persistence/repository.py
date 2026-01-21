from abc import ABC, abstractmethod

class Repository(ABC):
    """
    Abstract Base Class for the Repository pattern.

    This class defines the standard interface for data persistence operations.
    """
    @abstractmethod
    def add(self, obj):
        """
        Add a new object to the repository.

        Args:
            obj (object): The entity object to be stored. The object is expected 
            to have a unique 'id' attribute.
        """
        pass

    @abstractmethod
    def get(self, obj_id):
        """
        Retrieve an object by its unique identifier.

        Args:
            obj_id (str): The unique ID of the object.

        Returns:
            object: The found object, or None if it does not exist.
        """
        pass

    @abstractmethod
    def get_all(self):
        """
        Retrieve all objects stored in the repository.

        Returns:
            list: A list containing all stored objects.
        """
        pass

    @abstractmethod
    def update(self, obj_id, data):
        """
        Update an existing object with new data.

        Args:
            obj_id (str): The unique ID of the object to update.
            data (dict): A dictionary or data structure containing the updates.
        """
        pass

    @abstractmethod
    def delete(self, obj_id):
        """
        Remove an object from the repository.

        Args:
            obj_id (str): The unique ID of the object to delete.
        """
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        """
        Retrieve an object based on a specific attribute value.

        Args:
            attr_name (str): The name of the attribute to filter by.
            attr_value (any): The value of the attribute to match.

        Returns:
            object: The first object matching the criteria, or None if not found.
        """
        pass


class InMemoryRepository(Repository):
    """
    An implementation of the Repository interface using in-memory storage.
    """
    def __init__(self):
        """Initialize the repository with an empty dictionary storage."""
        self._storage = {}

    def add(self, obj):
        """
        Add an object to the in-memory storage.
        
        Uses the object's 'id' attribute as the dictionary key.
        """
        self._storage[obj.id] = obj

    def get(self, obj_id):
        """
        Retrieve an object from storage by ID.
        
        Returns None if the key is missing.
        """
        return self._storage.get(obj_id)

    def get_all(self):
        """
        Return a list of all objects in storage.
        """
        return list(self._storage.values())

    def update(self, obj_id, data):
        """
        Update an object in storage.

        Args:
            obj_id (str): The ID of the object.
            data (dict): Data to be passed to the object's update method.
        """
        obj = self.get(obj_id)
        if obj:
            obj.update(data)

    def delete(self, obj_id):
        """
        Remove the object with the given ID from storage if it exists.
        """
        if obj_id in self._storage:
            del self._storage[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        """
        Scan all objects in storage to find the first match for a specific attribute.

        Returns:
            object: The first matching object, or None if no match is found.
        """
        return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None) 
    
from app.extensions import db
from app.models import User, Place, Review, Amenity 

class SQLAlchemyRepository(Repository):
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()

    def get(self, obj_id):
        return self.model.query.get(obj_id)

    def get_all(self):
        return self.model.query.all()

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db.session.commit()

    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get_by_attribute(self, attr_name, attr_value):
        return self.model.query.filter(getattr(self.model, attr_name) == attr_value).first()
