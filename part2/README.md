# HBnB - Part 2

## Business Logic and API Endpoints Implementation

### Project Structure
```
part2/
├── app/
│   ├── models/
│   │   ├── base_model.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── amenity.py
│   ├── api/
│   ├── services/
│   └── persistence/
└── README.md
```

### Core Classes

- **BaseModel**: Base class with id, created_at, updated_at
- **User**: User entity with name, email, admin status
- **Place**: Place entity with title, price, location, owner
- **Review**: Review entity with text, rating, place, user
- **Amenity**: Amenity entity with name

### Author
anoud75
