from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.persistence.user_repository import UserRepository
from app.persistence.place_repository import PlaceRepository
from app.persistence.review_repository import ReviewRepository
from app.persistence.amenity_repository import AmenityRepository

class HBnBFacade:
    """
    The Facade pattern class for the HBnB application.
    """
    def __init__(self):
        self.user_repository = UserRepository()
        self.place_repository = PlaceRepository()
        self.review_repository = ReviewRepository()
        self.amenity_repository = AmenityRepository()

    # ---- User ----
    def create_user(self, user_data):
        """Create a new user."""
        user = User(**user_data)
        user.hash_password(user_data['password']) 
        self.user_repository.add(user)
        return user
        
    def get_user(self, user_id):
        return self.user_repository.get(user_id)
    
    def get_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)
    
    def get_all_users(self):
        return self.user_repository.get_all()

    def update_user(self, user_id, user_data):
        user = self.user_repository.get(user_id)
        if user:
            if 'password' in user_data:
                user.hash_password(user_data['password'])
             
            self.user_repository.update(user_id, user_data)
            return user
        return None
    
    # ---- Amenity ----
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repository.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repository.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repository.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repository.get(amenity_id)
        if amenity:
           
            amenity.update(amenity_data) 
        return amenity

    # ---- Place ----
    def create_place(self, place_data):
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
            owner_id=owner_id
        )
        
        
        amenity_ids = place_data.get('amenities', [])
        for amenity_id in amenity_ids:
            amenity = self.get_amenity(amenity_id)
            if amenity:
                place.add_amenity(amenity)
        
        self.place_repository.add(place) 
        return place

    def get_place(self, place_id):
        return self.place_repository.get(place_id)

    def get_all_places(self):
        return self.place_repository.get_all()

    def update_place(self, place_id, place_data):
        """Update place details and persist changes."""
        place = self.place_repository.get(place_id)
        if place:
          
            for key, value in place_data.items():
                if key not in ['id', 'owner_id', 'amenities']:
                    setattr(place, key, value)
            
            
            if 'amenities' in place_data:
                place.amenities = [] 
                for amenity_id in place_data['amenities']:
                    amenity = self.get_amenity(amenity_id)
                    if amenity:
                        place.add_amenity(amenity)
            
           
            place.save()
            
        return place

    # --- Review ---
    def create_review(self, review_data):
        user = self.get_user(review_data['user_id'])
        place = self.get_place(review_data['place_id'])

        if not user:
            raise ValueError("User not found")
        if not place:
            raise ValueError("Place not found")
        
        review = Review(
            text=review_data['text'],
            rating=review_data['rating'],
            user_id=review_data['user_id'],
            place_id=review_data['place_id']
        )

        self.review_repository.add(review)
        return review
    
    def get_review(self, review_id):
        return self.review_repository.get(review_id)

    def get_all_reviews(self):
        return self.review_repository.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.get_place(place_id)
        if not place:
            return None
        return place.reviews

    def update_review(self, review_id, review_data):
        review = self.review_repository.get(review_id)
        if review:
            review.update(review_data) 
        return review

    def delete_review(self, review_id):
        self.review_repository.delete(review_id)