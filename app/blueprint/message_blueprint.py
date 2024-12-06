from flask import abort, jsonify
from flask_smorest import Blueprint
from app.repository.message_repo import MessageRepository
from app.schema.message_schema import MessageSchema

message_blp = Blueprint('message', 'message', url_prefix='/message', description="Operation for message")


@message_blp.route("/", methods=['POST'])
@message_blp.arguments(MessageSchema)
@message_blp.response(201, MessageSchema)
def create_message(data):
    message = MessageRepository.create_message(data)
    return message


@message_blp.route("/<string:user_id>", methods=['GET'])
@message_blp.response(200, MessageSchema)
def get_message_by_id(message_id):
    message = MessageRepository.get_message_by_id(message_id)
    if not message:
        return jsonify({"message": "not found"}), 404
    return message


@message_blp.route("/", methods=['GET'])
@message_blp.response(200, MessageSchema(many=True))
def get_all_message():
    message = MessageRepository.get_all()
    return message


@message_blp.route("/<string:user_id>", methods=['PUT'])
@message_blp.arguments(MessageSchema)
@message_blp.response(200, MessageSchema)
def update_message(data, message_id):
    message = MessageRepository.get_message_by_id(message_id)
    if not message:
        abort(description="User not found"), 404
    updated_message = MessageRepository.update_message(message, data)

    return updated_message


@message_blp.route("/<string:user_id>", methods=['DELETE'])
@message_blp.response(204)
def delete_message(message_id):
    message = MessageRepository.get_message_by_id(message_id)

    if not message:
        abort(description="Message Not Found"), 404
    MessageRepository.delete_message(message)
    return ''