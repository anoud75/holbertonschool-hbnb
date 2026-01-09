# HBnB - Part 2

Business Logic and API Endpoints Implementation

## Project Structure
```
hbnb/
├── app/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── __pycache__/
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       └── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── base.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   └── facade.py
│   └── persistence/
│       ├── __init__.py
│       ├── __pycache__/
│       └── repository.py
├── test/
│   ├── __init__.py
│   └── test_api.py
├── run.py
├── config.py
├── requirements.txt
├── test_logic.py
└── README.md
```

## Installation
```bash
pip install -r requirements.txt
```

## Run Application
```bash
python run.py
```

Application available at: `http://127.0.0.1:5000`

## API Documentation

Interactive Swagger UI: `http://127.0.0.1:5000/api/v1/docs`

## Core Features

- **User Management**: Registration and profile management
- **Place Listings**: Property creation and management
- **Review System**: User reviews with ratings (1-5)
- **Amenities**: Property features and facilities

## Technologies

- Flask
- Flask-RESTx
- Python 3.10

## Authors

- Amaal AlOtaibi
- Alanoud Alsmail
- Norah Alnujidi
