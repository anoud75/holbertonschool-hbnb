-- HBnB Complete Database Setup
-- Run this script to create the schema and insert initial data

-- Include schema
.read schema.sql

-- Include seed data
.read seed.sql

-- Verify setup
SELECT '=== DATABASE SETUP COMPLETE ===' AS '';
SELECT 'Users: ' || COUNT(*) FROM users;
SELECT 'Places: ' || COUNT(*) FROM places;
SELECT 'Amenities: ' || COUNT(*) FROM amenities;
SELECT 'Reviews: ' || COUNT(*) FROM reviews;
