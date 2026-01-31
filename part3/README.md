
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

## Database Diagrams

### ER Diagram
The Entity-Relationship diagram is documented in `er_diagram.md` and can be viewed:
- Directly on GitHub (renders Mermaid automatically)
- Using the [Mermaid Live Editor](https://mermaid.live)
- In VS Code with the Mermaid extension

### Files
- `er_diagram.md` - Complete ER diagram with documentation
- `schema_diagram.mermaid` - Standalone Mermaid diagram file
- `class_diagram.md` - UML class diagram showing SQLAlchemy relationships

### Viewing the Diagrams

#### Option 1: GitHub
GitHub automatically renders Mermaid diagrams in markdown files.

#### Option 2: Mermaid Live Editor
1. Go to https://mermaid.live
2. Copy the content from `schema_diagram.mermaid`
3. Paste it in the editor to view and export

#### Option 3: VS Code
Install the "Markdown Preview Mermaid Support" extension.

### Diagram Summary
```
┌─────────┐     owns      ┌─────────┐
│  USER   │───────────────│  PLACE  │
└─────────┘               └─────────┘
     │                         │
     │ writes                  │ has
     │                         │
     ▼                         ▼
┌─────────┐               ┌─────────┐
│ REVIEW  │               │ AMENITY │
└─────────┘               └─────────┘
                               │
                    ┌──────────┴──────────┐
                    │   PLACE_AMENITY     │
                    │  (Junction Table)   │
                    └─────────────────────┘
```
