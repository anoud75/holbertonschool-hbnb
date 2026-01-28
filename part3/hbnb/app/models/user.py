from app.models.base import BaseModel
from app.extensions import bcrypt, db
from sqlalchemy.orm import validates
import re

class User(BaseModel):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # def __init__(self, **kwargs):
    #     if 'password' in kwargs:
    #         kwargs['password'] = bcrypt.generate_password_hash(kwargs['password']).decode('utf-8')
    #     super().__init__(**kwargs)

    @validates('email')
    def validate_email(self, key, email):
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not email or not re.match(email_regex, email):
            raise ValueError("Invalid email format")
        return email

    @validates('first_name', 'last_name')
    def validate_names(self, key, name):
        if not name or len(name) > 50:
            raise ValueError(f"{key.replace('_', ' ').capitalize()} must be under 50 characters")
        return name

    def hash_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)