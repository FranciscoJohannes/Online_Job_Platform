from datetime import datetime
from app.models.application_model import ApplicationModel
from app.extension import db, bcrypt


class ApplicationRepository:

    @staticmethod
    def create_application(data):
        data["password"] = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
        application = ApplicationModel(**data)
        db.session.add(application)
        db.session.commit()
        return application

    @staticmethod
    def get_application_by_id(application_id):
        return ApplicationModel.query.get(application_id)


    @staticmethod
    def get_all():
        return ApplicationModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_application(application, data):
        for key, value in data.items():
            setattr(application, key, value)
        db.session.commit()
        return application

    @staticmethod
    def delete_application(application):
        application.deleted_at = datetime.utcnow()
        db.session.commit()