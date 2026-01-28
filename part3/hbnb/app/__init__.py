"""
This module contains the factory function `create_app` responsible for initializing
the Flask application and configuring the RESTful API extension (Flask-RESTx).

It aggregates the various API namespaces (Users, Amenities, Places, Reviews)
into a single application instance.
"""

from flask import Flask
from flask_restx import Api
from app.extensions import bcrypt, db, jwt
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.auth import api as auth_ns




def create_app(config_class="config.DevelopmentConfig"):
    """
    Create and configure the Flask application instance.

    This function implements the Application Factory pattern. It initializes the
    Flask app, sets up the Flask-RESTx API object with metadata (title, version,
    description), and registers the API namespaces (blueprints) for the
    application's different resources.

    The API documentation (Swagger UI) is configured to be served at the
    endpoint `/api/v1/`.

    Returns:
        Flask: The fully configured Flask application instance, ready to be run.
    """
    app = Flask(__name__)
    bcrypt.init_app(app)
    jwt.init_app(app)
    app.config.from_object(config_class)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')

    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(auth_ns, path='/api/v1/auth')
    return app