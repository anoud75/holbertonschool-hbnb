-- HBnB CRUD Operations Test Script

-- =====================================================
-- READ OPERATIONS (Verify Initial Data)
-- =====================================================

SELECT '=== ALL USERS ===';
SELECT id, first_name, last_name, email, is_admin FROM users;

SELECT '=== ALL AMENITIES ===';
SELECT id, name FROM amenities;

SELECT '=== ALL PLACES WITH OWNERS ===';
SELECT p.id, p.title, p.price, u.first_name || ' ' || u.last_name AS owner
FROM places p
JOIN users u ON p.owner_id = u.id;

SELECT '=== ALL REVIEWS ===';
SELECT r.rating, r.text, p.title AS place, u.first_name AS reviewer
FROM reviews r
JOIN places p ON r.place_id = p.id
JOIN users u ON r.user_id = u.id;

SELECT '=== PLACES WITH AMENITIES ===';
SELECT p.title, GROUP_CONCAT(a.name) AS amenities
FROM places p
LEFT JOIN place_amenity pa ON p.id = pa.place_id
LEFT JOIN amenities a ON pa.amenity_id = a.id
GROUP BY p.id;

-- =====================================================
-- CREATE OPERATIONS
-- =====================================================

SELECT '=== CREATING NEW USER ===';
INSERT INTO users (id, first_name, last_name, email, password_hash, is_admin)
VALUES ('test1234-test-test-test-test12345678', 'Test', 'User', 'test@example.com',
        '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/X4.qnQpKqH6fKjKuS', FALSE);

SELECT '=== CREATING NEW PLACE ===';
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id)
VALUES ('test-place-1111-1111-111111111111', 'Test Place', 'A test place',
        100.00, 35.6762, 139.6503, 'test1234-test-test-test-test12345678');

INSERT INTO place_amenity (place_id, amenity_id)
VALUES ('test-place-1111-1111-111111111111', 'a1b2c3d4-e5f6-7890-abcd-ef1234567890');

SELECT '=== CREATING NEW REVIEW ===';
INSERT INTO reviews (id, text, rating, place_id, user_id)
VALUES ('test-rev-1111-1111-111111111111', 'Great test place!', 4,
        'test-place-1111-1111-111111111111', '11111111-1111-1111-1111-111111111111');

SELECT '=== VERIFY NEW DATA ===';
SELECT * FROM users WHERE email = 'test@example.com';
SELECT * FROM places WHERE title = 'Test Place';
SELECT * FROM reviews WHERE text = 'Great test place!';

-- =====================================================
-- UPDATE OPERATIONS
-- =====================================================

SELECT '=== UPDATING USER ===';
UPDATE users SET first_name = 'Updated', updated_at = CURRENT_TIMESTAMP
WHERE email = 'test@example.com';

SELECT '=== UPDATING PLACE ===';
UPDATE places SET price = 125.00, updated_at = CURRENT_TIMESTAMP
WHERE title = 'Test Place';

SELECT '=== UPDATING REVIEW ===';
UPDATE reviews SET rating = 5, updated_at = CURRENT_TIMESTAMP
WHERE id = 'test-rev-1111-1111-111111111111';

SELECT '=== VERIFY UPDATES ===';
SELECT first_name FROM users WHERE email = 'test@example.com';
SELECT price FROM places WHERE title = 'Test Place';
SELECT rating FROM reviews WHERE id = 'test-rev-1111-1111-111111111111';

-- =====================================================
-- DELETE OPERATIONS
-- =====================================================

SELECT '=== DELETING TEST DATA ===';
DELETE FROM reviews WHERE id = 'test-rev-1111-1111-111111111111';
DELETE FROM places WHERE id = 'test-place-1111-1111-111111111111';
DELETE FROM users WHERE id = 'test1234-test-test-test-test12345678';

SELECT '=== VERIFY DELETIONS ===';
SELECT COUNT(*) AS 'Test users remaining' FROM users WHERE email = 'test@example.com';
SELECT COUNT(*) AS 'Test places remaining' FROM places WHERE title = 'Test Place';

SELECT '=== CRUD TESTS COMPLETED ===';
