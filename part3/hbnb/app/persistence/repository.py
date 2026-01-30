from abc import ABC, abstractmethod
from app.extensions import db

class Repository(ABC):
    """
    Abstract Base Class for the Repository pattern.
    """
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class SQLAlchemyRepository(Repository):
    """
    SQLAlchemy implementation of the Repository interface.
    """
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        """Add object to session and commit"""
        db.session.add(obj)
        db.session.commit()

    def get(self, obj_id):
        """Get object by Primary Key"""
        return self.model.query.get(obj_id)

    def get_all(self):
        """Get all objects"""
        return self.model.query.all()

    def update(self, obj_id, data):
        """Update object attributes"""
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
            db.session.commit()
            return obj
        return None

    def delete(self, obj_id):
        """Delete object"""
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get_by_attribute(self, attr_name, attr_value):
        """Get first object matching attribute"""
        filter_kwargs = {attr_name: attr_value}
        return self.model.query.filter_by(**filter_kwargs).first()