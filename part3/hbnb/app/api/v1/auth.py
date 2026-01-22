"""
Authentication endpoints for the HBnB application.
Handles user login and JWT token generation.
"""

from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services import facade

api = Namespace('auth', description='Authentication operations')

# Model for input validation
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})


@api.route('/login')
class Login(Resource):
    """
    Login resource for user authentication.
    Authenticates user credentials and issues JWT token.
    """

    @api.expect(login_model, validate=True)
    @api.response(200, 'Login successful, token returned')
    @api.response(401, 'Invalid credentials')
    @api.response(400, 'Invalid input data')
    def post(self):
        """
        Authenticate user and return a JWT token.
        
        Expected JSON payload:
        {
            "email": "user@example.com",
            "password": "password123"
        }
        
        Returns:
        {
            "access_token": "jwt_token_here"
        }
        """
        credentials = api.payload  # Get the email and password from request


        user = facade.get_user_by_email(credentials['email'])


        if not user or not user.verify_password(credentials['password']):
            return {'error': 'Invalid credentials'}, 401


        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"is_admin": user.is_admin}
        )

        
        return {'access_token': access_token}, 200
