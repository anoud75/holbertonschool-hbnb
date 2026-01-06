#!/usr/bin/python3
from app.persistence.repository import InMemoryRepository
from app.models.user import User

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def __init__(self):
        """Initialize repositories for each entity."""
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # User methods
    def create_user(self, user_data):
        """
        Create a new user.
        
        Args:
            user_data: Dictionary containing user information
            
        Returns:
            Created User object
        """
        user = User(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            password=user_data['password'],
            is_admin=user_data.get('is_admin', False)
        )
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """
        Retrieve a user by ID.
        
        Args:
            user_id: Unique identifier of the user
            
        Returns:
            User object or None if not found
        """
        return self.user_repo.get(user_id)

    def get_all_users(self):
        """
        Retrieve all users.
        
        Returns:
            List of all User objects
        """
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        """
        Update user information.
        
        Args:
            user_id: Unique identifier of the user
            user_data: Dictionary containing updated user information
            
        Returns:
            Updated User object or None if not found
        """
        user = self.user_repo.get(user_id)
        if user:
            user.update(user_data)
        return user

    def get_user_by_email(self, email):
        """
        Retrieve a user by email.
        
        Args:
            email: Email address of the user
            
        Returns:
            User object or None if not found
        """
        return self.user_repo.get_by_attribute('email', email)

    # Placeholder methods for other entities (will be implemented later)
    def create_place(self, place_data):
        """Placeholder for place creation."""
        pass

    def get_place(self, place_id):
        """Placeholder for fetching a place by ID."""
        pass

    def create_amenity(self, amenity_data):
        """Placeholder for amenity creation."""
        pass

    def create_review(self, review_data):
        """Placeholder for review creation."""
        pass 
