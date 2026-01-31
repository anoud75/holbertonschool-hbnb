# HBnB Class Diagram

## Class Relationships with SQLAlchemy
```mermaid
classDiagram
    class BaseModel {
        +String id
        +DateTime created_at
        +DateTime updated_at
        +save()
        +delete()
        +to_dict()
    }

    class User {
        +String first_name
        +String last_name
        +String email
        +String password_hash
        +Boolean is_admin
        +List~Place~ places
        +List~Review~ reviews
        +hash_password(password)
        +verify_password(password)
    }

    class Place {
        +String title
        +String description
        +Float price
        +Float latitude
        +Float longitude
        +String owner_id
        +User owner
        +List~Review~ reviews
        +List~Amenity~ amenities
        +add_amenity(amenity)
        +remove_amenity(amenity)
    }

    class Review {
        +String text
        +Integer rating
        +String place_id
        +String user_id
        +Place place
        +User user
    }

    class Amenity {
        +String name
        +List~Place~ places
    }

    BaseModel <|-- User
    BaseModel <|-- Place
    BaseModel <|-- Review
    BaseModel <|-- Amenity

    User "1" --o "*" Place : owns
    User "1" --o "*" Review : writes
    Place "1" --o "*" Review : has
    Place "*" --o "*" Amenity : has
```

## Relationship Details

### Inheritance
All entity classes inherit from `BaseModel`, which provides:
- UUID generation for `id`
- Automatic timestamps (`created_at`, `updated_at`)
- Common methods (`save()`, `delete()`, `to_dict()`)

### Association Types

| Relationship | Type | Implementation |
|--------------|------|----------------|
| User → Place | One-to-Many | `db.relationship()` with `backref='owner'` |
| User → Review | One-to-Many | `db.relationship()` with `backref='user'` |
| Place → Review | One-to-Many | `db.relationship()` with `backref='place'` |
| Place ↔ Amenity | Many-to-Many | Association table `place_amenity` |
