from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

def hbnb_tesr():
    print("--- test start ---")

    try:
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.email == "john.doe@example.com"
        assert user.is_admin is False  # Default value
        print("User creation test passed!")
    except Exception as e:
        print(f"User creation failed: {e}")




    try:
        owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
        place = Place(title="Cozy Apartment", description="A nice place to stay", price=100, latitude=37.7749, longitude=-122.4194, owner=owner)
        print("Place creation and relationship test passed!")
    except Exception as e:
        print(f"Place creation failed: {e}")

    try:
        # Adding a review
        review = Review(text="Great stay!", rating=5, place=place, user=owner)
        place.add_review(review)

        assert place.title == "Cozy Apartment"
        assert place.price == 100
        assert len(place.reviews) == 1
        assert place.reviews[0].text == "Great stay!"
        print("review creation and relationship test passed!")
    except Exception as e:
        print(f"review creation failed: {e}")



    try:
        amenity = Amenity(name="Wi-Fi")
        assert amenity.name == "Wi-Fi"
        print("Amenity creation test passed!")
    except Exception as e:
        print(f"Amenity creation failed: {e}")

    print("--- Tests Completed ---")

if __name__ == "__main__":
    hbnb_tesr()

