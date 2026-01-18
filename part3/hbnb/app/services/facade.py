from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

class HBnBFacade:
    """
    The Facade pattern class for the HBnB application.
    """
    def __init__(self):
        """
        Initialize the Facade with in-memory repositories for each entity type.
        """
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # ---- User ----
    def create_user(self, user_data):
        """
        Create a new user and add it to the repository.

        Args:
            user_data: containing user attributes 
            (first_name, last_name, email, etc.).

        Returns:
            User: The created User object.
        """
        user = User(**user_data)
        self.user_repo.add(user)
        return user
    
    def get_user(self, user_id):
        """
        Retrieve a user by their unique ID.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            User: The User object if found, else None.
        """
        return self.user_repo.get(user_id)
    
    def get_user_by_email(self, email):
        """
        Retrieve a user by their email address.

        Args:
            email (str): The email address to search for.

        Returns:
            User: The User object if found, else None.
        """
        return self.user_repo.get_by_attribute('email', email)
    
    def get_all_users(self):
        """
        Retrieve all registered users.

        Returns:
            list: A list of all User objects.
        """
        return self.user_repo.get_all()
    
    def update_user(self, user_id, user_data):
        """
        Update user details. 
        
        Args:
            user_id (str): The ID of the user to update.
            user_data (dict): Dictionary of attributes to update.

        Returns:
            User: The updated User object, or None if the user does not exist.
        """
        user = self.user_repo.get(user_id)
        if user:
            for key, value in user_data.items():
                if key != 'id' and key != 'email':
                     setattr(user, key, value)
        return user
    
    # ---- Amenity ----
    def create_amenity(self, amenity_data):
        """
        Create a new amenity (e.g., 'Wi-Fi', 'Pool').

        Args:
            amenity_data (dict): Dictionary containing amenity attributes (name).

        Returns:
            Amenity: The created Amenity object.
        """
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Retrieve an amenity by ID."""
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """Retrieve all available amenities."""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """
        Update an existing amenity.

        Args:
            amenity_id (str): The ID of the amenity.
            amenity_data (dict): Data to update.

        Returns:
            Amenity: The updated object, or None if not found.
        """
        amenity = self.amenity_repo.get(amenity_id)
        if amenity:
            amenity.update(amenity_data)
        return amenity

    # ---- Place ----
    def create_place(self, place_data):
        """
        Create a new Place listing.

        Args:
            place_data (dict): Dictionary containing place attributes. 
            Must contain 'owner_id', 'title', 'price', etc.

        Returns:
            Place: The created Place object.

        Raises:
            ValueError: If the specified owner_id does 
            not correspond to an existing user.
        """
        owner_id = place_data.get('owner_id')
        owner = self.get_user(owner_id)
        if not owner:
            raise ValueError("Owner not found")
        place = Place(
            title=place_data['title'],
            description=place_data.get('description', ''),
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            owner=owner
        )
        amenity_ids = place_data.get('amenities', [])
        for amenity_id in amenity_ids:
            amenity = self.get_amenity(amenity_id)
            if amenity:
                place.add_amenity(amenity)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """Retrieve a place by ID."""
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """Retrieve all places."""
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """
        Update place details.
        Args:
            place_id (str): ID of the place.
            place_data (dict): Attributes to update.

        Returns:
            Place: The updated object or None.
        """
        place = self.place_repo.get(place_id)
        if place:
            for key, value in place_data.items():
                if key != 'id' and key != 'owner_id' and key != 'amenities':
                    setattr(place, key, value)
            if 'amenities' in place_data:
                place.amenities = []
                for amenity_id in place_data['amenities']:
                    amenity = self.get_amenity(amenity_id)
                    if amenity:
                        place.add_amenity(amenity)
        return place
    

    # --- Review ---

    def create_review(self, review_data):
        """
        Create a review for a specific place by a specific user.

        Args:
            review_data (dict): Must contain 'user_id', 'place_id', 'text', and 'rating'.

        Returns:
            Review: The created Review object.

        Raises:
            ValueError: If the user_id or place_id are invalid.
        """
        user = self.get_user(review_data['user_id'])
        place = self.get_place(review_data['place_id'])

        if not user:
            raise ValueError("User not found")
        
        if not place:
            raise ValueError("Place not found")
        
        review = Review(
            text=review_data['text'],
            rating=review_data['rating'],
            place=place,
            user=user
        )

        self.review_repo.add(review)
        place.add_review(review)

        return review

    def get_review(self, review_id):
        """Retrieve a review by ID."""
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        """Retrieve all reviews in the system."""
        return self.amenity_repo.get_all()

    def get_reviews_by_place(self, place_id):
        """
        Retrieve all reviews associated with a specific place.
        
        Args:
            place_id (str): The ID of the place.
            
        Returns:
            list: List of Review objects, or None if place not found.
        """
        place = self.get_place(place_id)
        if not place:
            return None
        return place.reviews
    

    def update_review(self, review_id, review_data):
        """Update review details (text, rating)."""
        review = self.review_repo.get(review_id)
        if review:
            review.update(review_data)
        return review


    def delete_review(self, review_id):
        """
        Delete a review from the repository.
        
        Args:
            review_id (str): The ID of the review to delete.
        """
        review = self.review_repo.get(review_id)
        if review:
            self.review_repo.delete(review_id)
