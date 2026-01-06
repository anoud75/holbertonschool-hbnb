#!/usr/bin/python3
"""User API endpoints."""
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Input model
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'email': fields.String(required=True, description='Email'),
    'password': fields.String(required=True, description='Password')
})

# Output model
user_output = api.model('UserOutput', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name'),
    'last_name': fields.String(description='Last name'),
    'email': fields.String(description='Email'),
    'is_admin': fields.Boolean(description='Admin status'),
    'created_at': fields.String(description='Creation date'),
    'updated_at': fields.String(description='Update date')
})


@api.route('/')
class UserList(Resource):
    @api.marshal_list_with(user_output)
    def get(self):
        """Get all users"""
        users = facade.get_all_users()
        result = []
        for user in users:
            data = user.to_dict()
            data.pop('password', None)
            result.append(data)
        return result

    @api.expect(user_model)
    @api.marshal_with(user_output, code=201)
    def post(self):
        """Create a new user"""
        data = api.payload
        
        # Check email exists
        if facade.get_user_by_email(data['email']):
            api.abort(409, 'Email already registered')
        
        # Create user
        user = facade.create_user(data)
        result = user.to_dict()
        result.pop('password', None)
        return result, 201


@api.route('/<user_id>')
class UserResource(Resource):
    @api.marshal_with(user_output)
    def get(self, user_id):
        """Get user by ID"""
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, 'User not found')
        
        data = user.to_dict()
        data.pop('password', None)
        return data

    @api.expect(user_model)
    @api.marshal_with(user_output)
    def put(self, user_id):
        """Update user"""
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, 'User not found')
        
        data = api.payload
        
        # Check email conflict
        if 'email' in data:
            existing = facade.get_user_by_email(data['email'])
            if existing and existing.id != user_id:
                api.abort(409, 'Email already in use')
        
        # Update
        updated = facade.update_user(user_id, data)
        result = updated.to_dict()
        result.pop('password', None)
        return result
