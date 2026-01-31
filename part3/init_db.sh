#!/bin/bash
# HBnB Database Initialization Script

DB_FILE="hbnb_dev.db"

echo "=== HBnB Database Initialization ==="

# Remove existing database
if [ -f "$DB_FILE" ]; then
    echo "Removing existing database..."
    rm "$DB_FILE"
fi

# Create database and run schema
echo "Creating database schema..."
sqlite3 "$DB_FILE" < schema.sql

# Insert initial data
echo "Inserting initial data..."
sqlite3 "$DB_FILE" < seed.sql

# Verify setup
echo ""
echo "=== Database Setup Complete ==="
echo "Database file: $DB_FILE"
echo ""
sqlite3 "$DB_FILE" "SELECT 'Users: ' || COUNT(*) FROM users;"
sqlite3 "$DB_FILE" "SELECT 'Places: ' || COUNT(*) FROM places;"
sqlite3 "$DB_FILE" "SELECT 'Amenities: ' || COUNT(*) FROM amenities;"
sqlite3 "$DB_FILE" "SELECT 'Reviews: ' || COUNT(*) FROM reviews;"

echo ""
echo "To test CRUD operations, run:"
echo "sqlite3 $DB_FILE < test_crud.sql"
