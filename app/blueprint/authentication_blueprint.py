from flask import abort, jsonify
from flask_smorest import Blueprint
from app.repository.authentication_repo import AuthenticationRepository
from app.schema.authentication_schema import AuthenticationSchema

authentication_blp = Blueprint('authentication', 'authentication', url_prefix='/authentication', description="Operation for authentication")


@authentication_blp.route("/", methods=['POST'])
@authentication_blp.arguments(AuthenticationSchema)
@authentication_blp.response(201, AuthenticationSchema)
def create_authentication(data):
    authentication = AuthenticationRepository.create_authentication(data)
    return authentication


@authentication_blp.route("/<string:user_id>", methods=['GET'])
@authentication_blp.response(200, AuthenticationSchema)
def get_authentication_by_id(authentication_id):
    authentication = AuthenticationRepository.get_authentication_by_id(authentication_id)
    if not authentication:
        return jsonify({"message": "not found"}), 404
    return authentication


@authentication_blp.route("/", methods=['GET'])
@authentication_blp.response(200, AuthenticationSchema(many=True))
def get_authentication():
    authentication = AuthenticationRepository.get_all()
    return authentication


@authentication_blp.route("/<string:user_id>", methods=['PUT'])
@authentication_blp.arguments(AuthenticationSchema)
@authentication_blp.response(200, AuthenticationSchema)
def update_authentication(data, authentication_id):
    authentication = AuthenticationRepository.get_authentication_by_id(authentication_id)
    if not authentication:
        abort(description="Authentication not found"), 404
    updated_authentication = AuthenticationRepository.update_authentication(authentication, data)
    return updated_authentication


@authentication_blp.route("/<string:user_id>", methods=['DELETE'])
@authentication_blp.response(204)
def delete_authentication(interaction_id):
    authentication = AuthenticationRepository.get_authentication_by_id(interaction_id)

    if not authentication:
        abort(description="Authentication Not Found"), 404
    AuthenticationRepository.delete_authentication(authentication)
    return ''