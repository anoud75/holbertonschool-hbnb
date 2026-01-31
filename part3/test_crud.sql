-- HBnB CRUD Operations Test Script
-- This script tests Create, Read, Update, and Delete operations

-- =====================================================
-- READ OPERATIONS (Verify Initial Data)
-- =====================================================

-- Select all users
SELECT '=== ALL USERS ===' AS '';
SELECT id, first_name, last_name, email, is_admin FROM users;

-- Select all amenities
SELECT '=== ALL AMENITIES ===' AS '';
SELECT id, name FROM amenities;

-- Select all places with owner info
SELECT '=== ALL PLACES WITH OWNERS ===' AS '';
SELECT p.id, p.title, p.price, u.first_name || ' ' || u.last_name AS owner
FROM places p
JOIN users u ON p.owner_id = u.id;

-- Select all reviews with user and place info
SELECT '=== ALL REVIEWS ===' AS '';
SELECT r.rating, r.text, p.title AS place, u.first_name AS reviewer
FROM reviews r
JOIN places p ON r.place_id = p.id
JOIN users u ON r.user_id = u.id;

-- Select places with their amenities
SELECT '=== PLACES WITH AMENITIES ===' AS '';
SELECT p.title, GROUP_CONCAT(a.name) AS amenities
FROM places p
LEFT JOIN place_amenity pa ON p.id = pa.place_id
LEFT JOIN amenities a ON pa.amenity_id = a.id
GROUP BY p.id;

-- =====================================================
-- CREATE OPERATIONS
-- =====================================================

-- Insert a new user
SELECT '=== CREATING NEW USER ===' AS '';
INSERT INTO users (id, first_name, last_name, email, password_hash, is_admin)
VALUES ('test1234-test-test-test-test12345678', 'Test', 'User', 'test@example.com',
        '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/X4.qnQpKqH6fKjKuS', FALSE);

-- Insert a new place
SELECT '=== CREATING NEW PLACE ===' AS '';
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id)
VALUES ('test-place-1111-1111-111111111111', 'Test Place', 'A test place description',
        100.00, 35.6762, 139.6503, 'test1234-test-test-test-test12345678');

-- Link the new place with amenities
INSERT INTO place_amenity (place_id, amenity_id)
VALUES ('test-place-1111-1111-111111111111', 'a1b2c3d4-e5f6-7890-abcd-ef1234567890');

-- Insert a new review
SELECT '=== CREATING NEW REVIEW ===' AS '';
INSERT INTO reviews (id, text, rating, place_id, user_id)
VALUES ('test-rev-1111-1111-111111111111', 'Great test place!', 4,
        'test-place-1111-1111-111111111111', '11111111-1111-1111-1111-111111111111');

-- Verify new data
SELECT '=== VERIFY NEW USER ===' AS '';
SELECT id, first_name, last_name, email FROM users WHERE email = 'test@example.com';

SELECT '=== VERIFY NEW PLACE ===' AS '';
SELECT id, title, price FROM places WHERE title = 'Test Place';

SELECT '=== VERIFY NEW REVIEW ===' AS '';
SELECT id, text, rating FROM reviews WHERE text = 'Great test place!';

-- =====================================================
-- UPDATE OPERATIONS
-- =====================================================

-- Update user information
SELECT '=== UPDATING USER ===' AS '';
UPDATE users
SET first_name = 'Updated', last_name = 'Name', updated_at = CURRENT_TIMESTAMP
WHERE email = 'test@example.com';

-- Update place price
SELECT '=== UPDATING PLACE ===' AS '';
UPDATE places
SET price = 125.00, updated_at = CURRENT_TIMESTAMP
WHERE title = 'Test Place';

-- Update review rating
SELECT '=== UPDATING REVIEW ===' AS '';
UPDATE reviews
SET rating = 5, text = 'Updated review - Excellent!', updated_at = CURRENT_TIMESTAMP
WHERE id = 'test-rev-1111-1111-111111111111';

-- Verify updates
SELECT '=== VERIFY UPDATED USER ===' AS '';
SELECT first_name, last_name FROM users WHERE email = 'test@example.com';

SELECT '=== VERIFY UPDATED PLACE ===' AS '';
SELECT title, price FROM places WHERE title = 'Test Place';

SELECT '=== VERIFY UPDATED REVIEW ===' AS '';
SELECT text, rating FROM reviews WHERE id = 'test-rev-1111-1111-111111111111';

-- =====================================================
-- DELETE OPERATIONS
-- =====================================================

-- Delete review
SELECT '=== DELETING REVIEW ===' AS '';
DELETE FROM reviews WHERE id = 'test-rev-1111-1111-111111111111';

-- Delete place (will also delete associated amenity links due to CASCADE)
SELECT '=== DELETING PLACE ===' AS '';
DELETE FROM places WHERE id = 'test-place-1111-1111-111111111111';

-- Delete user
SELECT '=== DELETING USER ===' AS '';
DELETE FROM users WHERE id = 'test1234-test-test-test-test12345678';

-- Verify deletions
SELECT '=== VERIFY DELETIONS ===' AS '';
SELECT COUNT(*) AS 'Test users remaining' FROM users WHERE email = 'test@example.com';
SELECT COUNT(*) AS 'Test places remaining' FROM places WHERE title = 'Test Place';
SELECT COUNT(*) AS 'Test reviews remaining' FROM reviews WHERE id = 'test-rev-1111-1111-111111111111';

SELECT '=== CRUD TESTS COMPLETED ===' AS '';
