-- HBnB Initial Data
-- This script inserts the administrator user and initial amenities

-- Insert Administrator User
-- Password: admin1234 (hashed with bcrypt)
INSERT INTO users (id, first_name, last_name, email, password_hash, is_admin, created_at, updated_at)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'Admin',
    'HBnB',
    'admin@hbnb.io',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/X4.qnQpKqH6fKjKuS',
    TRUE,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);

-- Insert Initial Amenities
INSERT INTO amenities (id, name, created_at, updated_at) VALUES
    ('a1b2c3d4-e5f6-7890-abcd-ef1234567890', 'WiFi', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('b2c3d4e5-f6a7-8901-bcde-f12345678901', 'Swimming Pool', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('c3d4e5f6-a7b8-9012-cdef-123456789012', 'Air Conditioning', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('d4e5f6a7-b8c9-0123-def0-234567890123', 'Parking', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('e5f6a7b8-c9d0-1234-ef01-345678901234', 'Pet Friendly', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('f6a7b8c9-d0e1-2345-f012-456789012345', 'Kitchen', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('a7b8c9d0-e1f2-3456-0123-567890123456', 'Gym', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('b8c9d0e1-f2a3-4567-1234-678901234567', 'Washer/Dryer', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Insert Sample Users (for testing)
INSERT INTO users (id, first_name, last_name, email, password_hash, is_admin, created_at, updated_at)
VALUES
    ('11111111-1111-1111-1111-111111111111', 'John', 'Doe', 'john.doe@example.com',
     '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/X4.qnQpKqH6fKjKuS', FALSE,
     CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('22222222-2222-2222-2222-222222222222', 'Jane', 'Smith', 'jane.smith@example.com',
     '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/X4.qnQpKqH6fKjKuS', FALSE,
     CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Insert Sample Places
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id, created_at, updated_at)
VALUES
    ('aaaa1111-aaaa-1111-aaaa-111111111111', 'Cozy Downtown Apartment',
     'A beautiful apartment in the heart of the city with modern amenities.',
     150.00, 40.7128, -74.0060, '11111111-1111-1111-1111-111111111111',
     CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('bbbb2222-bbbb-2222-bbbb-222222222222', 'Beach House Paradise',
     'Stunning beach house with ocean views and private access to the beach.',
     300.00, 25.7617, -80.1918, '11111111-1111-1111-1111-111111111111',
     CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('cccc3333-cccc-3333-cccc-333333333333', 'Mountain Retreat Cabin',
     'Peaceful cabin in the mountains, perfect for hiking and relaxation.',
     200.00, 39.5501, -105.7821, '22222222-2222-2222-2222-222222222222',
     CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Link Places with Amenities
INSERT INTO place_amenity (place_id, amenity_id) VALUES
    ('aaaa1111-aaaa-1111-aaaa-111111111111', 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'),
    ('aaaa1111-aaaa-1111-aaaa-111111111111', 'c3d4e5f6-a7b8-9012-cdef-123456789012'),
    ('aaaa1111-aaaa-1111-aaaa-111111111111', 'f6a7b8c9-d0e1-2345-f012-456789012345'),
    ('bbbb2222-bbbb-2222-bbbb-222222222222', 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'),
    ('bbbb2222-bbbb-2222-bbbb-222222222222', 'b2c3d4e5-f6a7-8901-bcde-f12345678901'),
    ('bbbb2222-bbbb-2222-bbbb-222222222222', 'c3d4e5f6-a7b8-9012-cdef-123456789012'),
    ('bbbb2222-bbbb-2222-bbbb-222222222222', 'd4e5f6a7-b8c9-0123-def0-234567890123'),
    ('bbbb2222-bbbb-2222-bbbb-222222222222', 'f6a7b8c9-d0e1-2345-f012-456789012345'),
    ('cccc3333-cccc-3333-cccc-333333333333', 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'),
    ('cccc3333-cccc-3333-cccc-333333333333', 'e5f6a7b8-c9d0-1234-ef01-345678901234'),
    ('cccc3333-cccc-3333-cccc-333333333333', 'f6a7b8c9-d0e1-2345-f012-456789012345'),
    ('cccc3333-cccc-3333-cccc-333333333333', 'd4e5f6a7-b8c9-0123-def0-234567890123');

-- Insert Sample Reviews
INSERT INTO reviews (id, text, rating, place_id, user_id, created_at, updated_at)
VALUES
    ('rev11111-1111-1111-1111-111111111111',
     'Amazing apartment! Great location and very clean. Would definitely stay again.',
     5, 'aaaa1111-aaaa-1111-aaaa-111111111111', '22222222-2222-2222-2222-222222222222',
     CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('rev22222-2222-2222-2222-222222222222',
     'Beautiful beach house with stunning views. The private beach access was perfect.',
     5, 'bbbb2222-bbbb-2222-bbbb-222222222222', '22222222-2222-2222-2222-222222222222',
     CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('rev33333-3333-3333-3333-333333333333',
     'Cozy cabin in a great location. Perfect for a weekend getaway.',
     4, 'cccc3333-cccc-3333-cccc-333333333333', '11111111-1111-1111-1111-111111111111',
     CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
