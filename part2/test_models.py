#!/usr/bin/python3
"""Test the business logic classes."""
import sys
sys.path.insert(0, '/root/holbertonschool-hbnb/part2')

from app.models.base_model import BaseModel
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

# Test User
print("=== Testing User ===")
user1 = User("John", "Doe", "john@example.com")
print(f"User created: {user1.first_name} {user1.last_name}")
print(f"User ID: {user1.id}")
print(f"User email: {user1.email}")

# Test Amenity
print("\n=== Testing Amenity ===")
amenity1 = Amenity("WiFi")
amenity2 = Amenity("Pool")
print(f"Amenities: {amenity1.name}, {amenity2.name}")

# Test Place
print("\n=== Testing Place ===")
place1 = Place("Cozy Apartment", "A nice place", 100.0, 40.7128, -74.0060, user1)
print(f"Place: {place1.title}")
print(f"Price: ${place1.price}")
print(f"Owner: {place1.owner.first_name}")
place1.add_amenity(amenity1)
place1.add_amenity(amenity2)
print(f"Amenities: {[a.name for a in place1.amenities]}")

# Test Review
print("\n=== Testing Review ===")
user2 = User("Jane", "Smith", "jane@example.com")
review1 = Review("Great place!", 5, place1, user2)
print(f"Review by {user2.first_name}: {review1.text} ({review1.rating}/5)")

# Test to_dict
print("\n=== Testing to_dict ===")
print(f"User dict: {user1.to_dict()}")

print("\n=== All tests passed! ===")
