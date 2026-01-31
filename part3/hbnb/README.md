# HBnB Part 3: Enhanced Backend with Authentication and Database

## Overview

Part 3 adds JWT authentication and database integration to the HBnB application.

---

## Installation & Setup

```bash
pip install -r requirements.txt
python run.py
```

API available at: **http://localhost:5000/api/v1/**

---

## Authentication

### Login
```bash
POST /api/v1/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Protected Requests
Include token in Authorization header:
```bash
Authorization: Bearer {access_token}
```

---

## API Endpoints

### Users
- `POST /api/v1/users/` - Create user (public)
- `GET /api/v1/users/` - Get all users (public)
- `GET /api/v1/users/<user_id>` - Get user by ID (public)
- `PUT /api/v1/users/<user_id>` - Update user (authenticated, owner or admin)

### Places
- `POST /api/v1/places/` - Create place (authenticated)
- `GET /api/v1/places/` - Get all places (public)
- `GET /api/v1/places/<place_id>` - Get place by ID (public)
- `PUT /api/v1/places/<place_id>` - Update place (authenticated, owner or admin)
- `GET /api/v1/places/<place_id>/reviews` - Get reviews for a place (public)

### Reviews
- `POST /api/v1/reviews/` - Create review (authenticated)
- `GET /api/v1/reviews/` - Get all reviews (public)
- `GET /api/v1/reviews/<review_id>` - Get review by ID (public)
- `PUT /api/v1/reviews/<review_id>` - Update review (authenticated, owner only)
- `DELETE /api/v1/reviews/<review_id>` - Delete review (authenticated, owner only)

### Amenities
- `POST /api/v1/amenities/` - Create amenity (authenticated, admin only)
- `GET /api/v1/amenities/` - Get all amenities (public)
- `GET /api/v1/amenities/<amenity_id>` - Get amenity by ID (public)
- `PUT /api/v1/amenities/<amenity_id>` - Update amenity (authenticated, admin only)

### Authentication
- `POST /api/v1/auth/login` - Login and get JWT token

---

## Testing

### Create User
```bash
curl -X POST http://localhost:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Ahmed",
    "last_name": "Ali",
    "email": "ahmed@example.com",
    "password": "Pass123"
  }'
```

### Login
```bash
curl -X POST http://localhost:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "ahmed@example.com",
    "password": "Pass123"
  }'
```

---

## Project Structure

```
part3/hbnb/
├── app/
│   ├── api/v1/
│   │   ├── users.py
│   │   ├── places.py
│   │   ├── reviews.py
│   │   ├── amenities.py
│   │   └── auth.py
│   ├── models/
│   │   ├── base.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── amenity.py
│   ├── services/
│   │   └── facade.py
│   ├── persistence/
│   │   └── repository.py
│   ├── extensions.py
│   └── __init__.py
├── config.py
├── requirements.txt
├── run.py
└── development.db
```

---

## Requirements

```
flask
flask-restx
flask-bcrypt
flask-sqlalchemy
flask-jwt-extended
sqlalchemy
```

---

## Contributors

- Amaal AlOtaibi
- Alanoud Alsmail
- Norah Alnujidi
