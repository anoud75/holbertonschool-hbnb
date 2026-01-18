import unittest
from app import create_app

class TestHBnBEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    # --- User Tests ---
    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_create_user_invalid_email(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "not-an-email"
        })
        self.assertEqual(response.status_code, 400) # Should fail

    # --- Place Tests ---
    def test_create_place_invalid_price(self):
        user_resp = self.client.post('/api/v1/users/', json={
            "first_name": "Owner", "last_name": "User", "email": "owner@test.com"
        })
        owner_id = user_resp.json['id']

        response = self.client.post('/api/v1/places/', json={
            "title": "Bad Price House",
            "price": -50,
            "latitude": 10.0,
            "longitude": 10.0,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 400)

    # --- Review Tests ---
    def test_create_review(self):
        user_resp = self.client.post('/api/v1/users/', json={
            "first_name": "Reviewer", "last_name": "Guy", "email": "reviewer@test.com"
        })
        user_id = user_resp.json['id']

        place_resp = self.client.post('/api/v1/places/', json={
            "title": "Nice Hotel", "price": 100, "latitude": 10, "longitude": 10,
            "owner_id": user_id
        })
        place_id = place_resp.json['id']

        response = self.client.post('/api/v1/reviews/', json={
            "text": "Great stay!",
            "rating": 5,
            "user_id": user_id,
            "place_id": place_id
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()