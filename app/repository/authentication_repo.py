from datetime import datetime
from app.models.authentication_model import AuthenticationModel
from app.extension import db


class AuthenticationRepository:

    @staticmethod
    def create_authentication(data):
        authentication = AuthenticationModel(**data)
        db.session.add(authentication)
        db.session.commit()

    @staticmethod
    def get_authentication_by_id(authentication_id ):
        return AuthenticationModel.query.filter_by(authentication_id=authentication_id ).first()

    @staticmethod
    def get_all():
        return AuthenticationModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_authentication(authentication, data):
        for key, value in data.items():
            setattr(authentication, key, value)
        db.session.commit()
        return authentication

    @staticmethod
    def delete_authentication(authentication):
        authentication.deleted_at = datetime.utcnow()
        db.session.commit()