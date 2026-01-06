#!/usr/bin/python3
"""User API endpoints."""
from flask_restx import Namespace, Resource, fields
from app.services import facade

# Create namespace for users
api = Namespace('users', description='User operations')

# Define the user input model for POST requests
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user', example='John'),
    'last_name': fields.String(required=True, description='Last name of the user', example='Doe'),
    'email': fields.String(required=True, description='Email of the user', example='john.doe@example.com'),
    'password': fields.String(required=True, description='Password of the user (min 6 characters)', example='password123')
})

# Define the user output model (without password)
user_output_model = api.model('UserOutput', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name'),
    'last_name': fields.String(description='Last name'),
    'email': fields.String(description='Email'),
    'is_admin': fields.Boolean(description='Admin status'),
    'created_at': fields.String(description='Creation timestamp'),
    'updated_at': fields.String(description='Last update timestamp')
})

# Define the update model (all fields optional)
user_update_model = api.model('UserUpdate', {
    'first_name': fields.String(description='First name of the user'),
    'last_name': fields.String(description='Last name of the user'),
    'email': fields.String(description='Email of the user'),
    'password': fields.String(description='Password of the user (min 6 characters)')
})


@api.route('/')
class UserList(Resource):
    """Handles operations on the user collection."""

    @api.doc('list_users')
    @api.marshal_list_with(user_output_model)
    def get(self):
        """
        Retrieve a list of all users.
        
        Returns:
            200: List of all users (passwords excluded)
        """
        users = facade.get_all_users()
        
        # Convert users to dict and exclude passwords
        users_data = []
        for user in users:
            user_dict = user.to_dict()
            user_dict.pop('password', None)  # Remove password for security
            users_data.append(user_dict)
        
        return users_data, 200

    @api.doc('create_user')
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created', user_output_model)
    @api.response(400, 'Invalid input data')
    @api.response(409, 'Email already registered')
    def post(self):
        """
        Register a new user.
        
        Returns:
            201: User successfully created
            400: Invalid input data
            409: Email already registered
        """
        user_data = api.payload

        # Validate required fields
        required_fields = ['first_name', 'last_name', 'email', 'password']
        for field in required_fields:
            if field not in user_data or not user_data[field]:
                return {'error': f'{field} is required'}, 400

        # Validate email format
        email = user_data['email']
        if '@' not in email or '.' not in email:
            return {'error': 'Invalid email format'}, 400

        # Check if email already exists
        existing_user = facade.get_user_by_email(email)
        if existing_user:
            return {'error': 'Email already registered'}, 409

        # Validate password length
        if len(user_data['password']) < 6:
            return {'error': 'Password must be at least 6 characters long'}, 400

        try:
            # Create new user
            new_user = facade.create_user(user_data)
            
            # Prepare response (exclude password)
            response_data = new_user.to_dict()
            response_data.pop('password', None)
            
            return response_data, 201

        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'An error occurred while creating the user'}, 500


@api.route('/<user_id>')
@api.param('user_id', 'The User unique identifier')
@api.response(404, 'User not found')
class UserResource(Resource):
    """Handles operations on a single user."""

    @api.doc('get_user')
    @api.marshal_with(user_output_model)
    def get(self, user_id):
        """
        Get user details by ID.
        
        Args:
            user_id: The unique identifier of the user
            
        Returns:
            200: User data (password excluded)
            404: User not found
        """
        user = facade.get_user(user_id)
        
        if not user:
            api.abort(404, 'User not found')
        
        # Convert to dict and exclude password
        user_data = user.to_dict()
        user_data.pop('password', None)
        
        return user_data, 200

    @api.doc('update_user')
    @api.expect(user_update_model, validate=True)
    @api.response(200, 'User successfully updated', user_output_model)
    @api.response(400, 'Invalid input data')
    @api.response(404, 'User not found')
    @api.response(409, 'Email already in use by another user')
    def put(self, user_id):
        """
        Update user information.
        
        Args:
            user_id: The unique identifier of the user
            
        Returns:
            200: User successfully updated
            400: Invalid input data
            404: User not found
            409: Email already in use
        """
        # Check if user exists
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, 'User not found')

        update_data = api.payload

        # Validate that at least one field is provided
        if not update_data:
            return {'error': 'No data provided for update'}, 400

        # Validate email if provided
        if 'email' in update_data:
            email = update_data['email']
            
            # Check email format
            if '@' not in email or '.' not in email:
                return {'error': 'Invalid email format'}, 400
            
            # Check if email is already used by another user
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email already in use by another user'}, 409

        # Validate password length if provided
        if 'password' in update_data:
            if len(update_data['password']) < 6:
                return {'error': 'Password must be at least 6 characters long'}, 400

        # Validate name fields if provided
        if 'first_name' in update_data and not update_data['first_name']:
            return {'error': 'First name cannot be empty'}, 400

        if 'last_name' in update_data and not update_data['last_name']:
            return {'error': 'Last name cannot be empty'}, 400

        try:
            # Update user through facade
            updated_user = facade.update_user(user_id, update_data)
            
            # Prepare response (exclude password)
            response_data = updated_user.to_dict()
            response_data.pop('password', None)
            
            return response_data, 200

        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'An error occurred while updating the user'}, 500 
