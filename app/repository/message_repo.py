from datetime import datetime
from app.models.message_model import MessageModel
from app.extension import db, bcrypt


class MessageRepository:

    @staticmethod
    def create_message(data):
        data["password"] = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
        message = MessageModel(**data)
        db.session.add(message)
        db.session.commit()
        return message

    @staticmethod
    def get_message_by_id(message_id):
        return MessageModel.query.get(message_id)


    @staticmethod
    def get_all():
        return MessageModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_message(message, data):
        for key, value in data.items():
            setattr(message, key, value)
        db.session.commit()
        return message

    @staticmethod
    def delete_message(message):
        message.deleted_at = datetime.utcnow()
        db.session.commit()