from app.models.base import BaseModel
import re
from app.extensions import bcrypt

class User(BaseModel):
    """
    Represents a User in the HBnB application.

    This class manages user identity and administrative status. It inherits 
    common attributes (like ID, created_at) from BaseModel and strictly validates 
    input data such as email format and name length.
    """
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        """
        Initialize a new User.

        Args:
            first_name (str): The user's first name (max 50 chars).
            last_name (str): The user's last name (max 50 chars).
            email (str): A valid email address.
            password (str): encrypted string serve as a user password
            is_admin (bool, optional): Administrative privilege flag. Defaults to False.

        Raises:
            ValueError: If name length exceeds limits or email format is invalid.
        """
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hash_password(password)
        self.is_admin = is_admin

    @property
    def first_name(self):
        """Get the user's first name."""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """
        Set the first name with validation.

        Args:
            value (str): The new first name.

        Raises:
            ValueError: If the value is empty or exceeds 50 characters.
        """
        if not value or len(value) > 50:
            raise ValueError("First name must be provided and under 50 characters")
        self._first_name = value

    @property
    def last_name(self):
        """Get the user's last name."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """
        Set the last name with validation.

        Args:
            value (str): The new last name.

        Raises:
            ValueError: If the value is empty or exceeds 50 characters.
        """
        if not value or len(value) > 50:
            raise ValueError("Last name must be provided and under 50 characters")
        self._last_name = value

    @property
    def email(self):
        """Get the user's email address."""
        return self._email

    @email.setter
    def email(self, value):
        """
        Set the email with Regex validation.

        Validates the email against a standard pattern (user@domain.tld).

        Args:
            value (str): The email address to set.

        Raises:
            ValueError: If the email format is invalid or empty.
        """
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not value or not re.match(email_regex, value):
            raise ValueError("Invalid email format")
        self._email = value


    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password)


    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

