from datetime import datetime
from app.models.job_interaction_table_model import JobInteractionTableModel
from app.extension import db, bcrypt


class JobInteractionTableRepository:

    @staticmethod
    def create_job_interaction_table(data):
        data["password"] = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
        job_interaction_table = JobInteractionTableModel(**data)
        db.session.add(job_interaction_table)
        db.session.commit()
        return job_interaction_table

    @staticmethod
    def get_job_interaction_table_by_id(interaction_id):
        return JobInteractionTableModel.query.get(interaction_id)


    @staticmethod
    def get_all():
        return JobInteractionTableModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_job_interaction_table(job_interaction_table, data):
        for key, value in data.items():
            setattr(job_interaction_table, key, value)
        db.session.commit()
        return job_interaction_table

    @staticmethod
    def delete_job_interaction_table(job_interaction_table):
        job_interaction_table.deleted_at = datetime.utcnow()
        db.session.commit()