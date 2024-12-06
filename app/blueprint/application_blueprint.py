from flask import abort, jsonify
from flask_smorest import Blueprint
from app.repository.application_repo import ApplicationRepository
from app.schema.application_schema import ApplicationSchema

application_blp = Blueprint('application', 'application', url_prefix='/application', description="Operation for application")


@application_blp.route("/", methods=['POST'])
@application_blp.arguments(ApplicationSchema)
@application_blp.response(201, ApplicationSchema)
def create_application(data):
    application = ApplicationRepository.create_application(data)
    return application


@application_blp.route("/<string:user_id>", methods=['GET'])
@application_blp.response(200, ApplicationSchema)
def get_application_by_id(application_id):
    application = ApplicationRepository.get_application_by_id(application_id)
    if not application:
        return jsonify({"message": "not found"}), 404
    return  application


@application_blp.route("/", methods=['GET'])
@application_blp.response(200, ApplicationSchema(many=True))
def get_application():
    application = ApplicationRepository.get_all()
    return application


@application_blp.route("/<string:user_id>", methods=['PUT'])
@application_blp.arguments(ApplicationSchema)
@application_blp.response(200, ApplicationSchema)
def update_authentication(data, authentication_id):
    application = ApplicationRepository.get_application_by_id(authentication_id)
    if not application:
        abort(description="Application not found"), 404
    updated_application = ApplicationRepository.update_application(application, data)
    return updated_application


@application_blp.route("/<string:user_id>", methods=['DELETE'])
@application_blp.response(204)
def delete_authentication(interaction_id):
    application = ApplicationRepository.get_application_by_id(interaction_id)

    if not application:
        abort(description="Authentication Not Found"), 404
    ApplicationRepository.delete_application(application)
    return ''