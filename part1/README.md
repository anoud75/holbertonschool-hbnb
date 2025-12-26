# Part 1: Architecture & Business Logic Design
This section contains the foundational architectural documentation for the HBnB application.

# High-Level Package Diagram
Objective
Illustrate the three-layer architecture of the HBnB application and demonstrate communication between layers using the Facade pattern.

## Architecture Overview
The HBnB application is structured using a layered architecture with three distinct layers:
1. Presentation Layer (Services, API)
2. Business Logic Layer (Models)
3. Persistence Layer (Database)


### The Facade Pattern
The Facade Pattern serves as the communication interface between layers, providing:

- Simplified Interface: Unified access point for layer interactions
- Decoupling: Layers remain independent and loosely coupled
- Flexibility: Easy to modify internal implementations without affecting other layers
- Maintainability: Centralized control of inter-layer communication


# Class Diagram
Objective
Design a comprehensive class diagram depicting the entities in the Business Logic layer, including their attributes, methods, and relationships.

## Core Entities
### 1. User Entity
Purpose: Represents application users who can create places and write reviews
Key Attributes:

id (UUID4) - Unique identifier
email (String) - User email address
password (String) - Hashed password
first_name (String) - User's first name
last_name (String) - User's last name
created_at (DateTime) - Account creation timestamp
updated_at (DateTime) - Last update timestamp

Key Methods:

register() - Create new user account
authenticate() - Verify user credentials
update_profile() - Modify user information

### 2. Place Entity
Purpose: Represents property listings created by users
Key Attributes:

id (UUID4) - Unique identifier
title (String) - Place title
description (Text) - Detailed description
price (Decimal) - Price per night
latitude (Float) - Geographic coordinate
longitude (Float) - Geographic coordinate
owner_id (UUID4) - Reference to User
created_at (DateTime) - Creation timestamp
updated_at (DateTime) - Last update timestamp

Key Methods:

create() - Create new place listing
update() - Modify place details
delete() - Remove place listing
add_amenity() - Associate amenity with place

### 3. Review Entity
Purpose: Represents user feedback on places
Key Attributes:

id (UUID4) - Unique identifier
rating (Integer) - Rating score (1-5)
comment (Text) - Review text
user_id (UUID4) - Reference to User
place_id (UUID4) - Reference to Place
created_at (DateTime) - Creation timestamp
updated_at (DateTime) - Last update timestamp

Key Methods:

submit() - Create new review
update() - Modify review
delete() - Remove review

### 4. Amenity Entity
Purpose: Represents features/facilities associated with places
Key Attributes:

id (UUID4) - Unique identifier
name (String) - Amenity name
description (String) - Amenity description
created_at (DateTime) - Creation timestamp
updated_at (DateTime) - Last update timestamp

Key Methods:

create() - Add new amenity type
update() - Modify amenity details


# API Sequence Diagrams
Overview
Each sequence diagram demonstrates:

Request Flow: How API requests travel through system layers
Layer Interactions: Communication between Presentation, Business Logic, and Persistence layers
Data Processing: Validation, transformation, and storage operations
Response Flow: How results are returned to the client

### 1. User Registration
Description
This sequence diagram illustrates the process of a new user registering for an account in the HBnB application.
Key Steps

User submits registration data (email, password, name)
API validates input format and required fields
Business Logic checks for duplicate email
Password is hashed for security
User data is saved to database
Confirmation response is returned

### Flow Explanation

Validation Layer: API validates request format before passing to business logic
Duplication Check: System ensures email uniqueness before creating account
Security: Password is hashed before storage, never stored in plain text
Response: User receives confirmation with their new user ID

## 2. Place Creation
Description
This sequence diagram shows how a user creates a new place listing in the system.
Key Steps

Authenticated user submits place details
API verifies user authentication token
Business Logic validates place data and ownership
Place is saved with owner reference
Place details are returned to user

### Flow Explanation

Authentication: User must be authenticated to create a place
Ownership: Place is automatically linked to the authenticated user
Validation: Price, coordinates, and required fields are validated
Amenities: Multiple amenities can be associated with the place
Response: Complete place details including relationships are returned

## 3. Review Submission
Description
This sequence diagram demonstrates how a user submits a review for a place they've visited.
Key Steps

Authenticated user submits review with rating and comment
System verifies user is authenticated
Business Logic validates place exists and user hasn't already reviewed it
Review is saved with references to user and place
Review details are returned

### Flow Explanation

Authentication: User must be logged in to submit a review
Place Validation: System ensures the place exists before accepting review
Duplicate Prevention: Users cannot submit multiple reviews for the same place
Owner Restriction: Place owners cannot review their own listings
Rating Update: Place's overall rating is recalculated after new review
Response: Complete review details with user and place information

## 4. Fetching a List of Places
Description
This sequence diagram shows how the system retrieves and returns a filtered list of places based on user criteria.
Key Steps

User requests places with optional filters (location, price, amenities)
API processes query parameters
Business Logic applies filters and sorting
Database returns matching places
Results are formatted and returned to user

### Flow Explanation

Query Parameters: API accepts multiple optional filters for flexible searching
Validation: Parameters are validated before processing (price ranges, coordinates)
Multiple Filters: System can apply price, location, and amenity filters simultaneously
Distance Calculation: Geographic distance is calculated when location filters are used
Enrichment: Each place is enriched with owner details, amenities, and average rating
Pagination: Results are paginated to improve performance and user experience
Response: Formatted list with complete place information and pagination metadata
