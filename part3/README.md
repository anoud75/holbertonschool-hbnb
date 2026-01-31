
## SQL Scripts

### Files
- `schema.sql` - Creates all database tables and relationships
- `seed.sql` - Inserts initial data (admin user, amenities, sample data)
- `test_crud.sql` - Tests CRUD operations
- `setup_database.sql` - Combined setup script
- `init_db.sh` - Shell script to initialize database

### Usage

#### Initialize Database
```bash
./init_db.sh
```

#### Or manually with SQLite
```bash
sqlite3 hbnb_dev.db < schema.sql
sqlite3 hbnb_dev.db < seed.sql
```

#### Test CRUD Operations
```bash
sqlite3 hbnb_dev.db < test_crud.sql
```

### Initial Data
- **Admin User**: admin@hbnb.io (password: admin1234)
- **Amenities**: WiFi, Swimming Pool, Air Conditioning, Parking, Pet Friendly, Kitchen, Gym, Washer/Dryer
- **Sample Users**: John Doe, Jane Smith
- **Sample Places**: 3 places with amenities and reviews
