#!/usr/bin/python3
from app.persistence.repository import InMemoryRepository
from app.models.user import User

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    ` def create_user(self, data):
        """Create user."""
        user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password']
        )
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Get user by ID."""
        return self.user_repo.get(user_id)

    def get_all_users(self):
        """Get all users."""
        return self.user_repo.get_all()

    def update_user(self, user_id, data):
        """Update user."""
        user = self.user_repo.get(user_id)
        if user:
            user.update(data)
        return user

    def get_user_by_email(self, email):
        """Get user by email."""
        return self.user_repo.get_by_attribute('email', email)
