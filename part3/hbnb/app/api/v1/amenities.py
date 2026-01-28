from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt


api = Namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    """
    Resource for managing the collection of amenities.
    Handles creation of new amenities and retrieval of the full list.
    """
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        amenity_data = api.payload

        new_amenity = facade.create_amenity(amenity_data)

        return {'id': new_amenity.id, 'name': new_amenity.name}, 201

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get_all_amenities()
        return[{'id': a.id, 'name': a.name} for a in amenities], 200

    @api.route('/<amenity_id>')
    class AmenityResource(Resource):
        @api.response(200, 'Amenity details retrieved successfully')
        @api.response(404, 'Amenity not found')
        def get(self, amenity_id):
            """Get amenity details by ID"""
            amenity = facade.get_amenity(amenity_id)
            if not amenity:
                return {'error': 'Amenity not found'}, 404
            return {'id': amenity.id, 'name': amenity.name}, 200

        @api.expect(amenity_model)
        @api.response(200, 'Amenity updated successfully')
        @api.response(404, 'Amenity not found')
        @api.response(400, 'Invalid input data')
        def put(self, amenity_id):
            """Update an amenity information"""
            amenity_data = api.payload

            amenity = facade.get_amenity(amenity_id)

            if not amenity:
                return {'error': 'Amenity not found'}, 404

            facade.update_amenity(amenity_id, amenity_data)

            return {'message': 'Amenity updated successfully'}, 200


@api.route('/amenities/')
class AdminAmenityCreate(Resource):
    @jwt_required
    def post(self):
        current_user = get_jwt()
        if not current_user.get("is_admin"):
            return {"error": "Admin privileges required"}, 403
        
        amenity = facade.create_amenity(api.payload)
        return {
            "id": amenity.id,
            "name": amenity.name
        }, 201

@api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    @jwt_required
    def put(self, amenity_id):
        current_user = get_jwt()
        if not current_user.get("is_admin"):
            return {"error": "Admin privileges required"}, 403
        
        facade.update_amenity(amenity_id, api.payload)
        return {"message": "Amenity update successfully"}, 200