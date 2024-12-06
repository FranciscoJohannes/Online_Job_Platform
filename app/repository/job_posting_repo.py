from datetime import datetime
from app.models.job_posting_model import JobPostingTableModel
from app.extension import db, bcrypt


class JobPostingRepository:

    @staticmethod
    def create_job_posting(data):
        data["password"] = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
        job_posting = JobPostingTableModel(**data)
        db.session.add(job_posting)
        db.session.commit()
        return job_posting

    @staticmethod
    def get_job_posting_by_id(job_id):
        return JobPostingTableModel.query.get(job_id)


    @staticmethod
    def get_all():
        return JobPostingTableModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_job_posting(job_posting, data):
        for key, value in data.items():
            setattr(job_posting, key, value)
        db.session.commit()
        return job_posting

    @staticmethod
    def delete_job_posting(job_posting):
        job_posting.deleted_at = datetime.utcnow()
        db.session.commit()

