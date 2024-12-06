from datetime import datetime
from app.models.job_performance_table_model import JobPerformanceModel
from app.extension import db, bcrypt


class JobPerformanceRepository:

    @staticmethod
    def create_job_performance(data):
        data["password"] = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
        job_performance = JobPerformanceModel(**data)
        db.session.add(job_performance)
        db.session.commit()
        return job_performance

    @staticmethod
    def get_job_performance_by_id(performance_id):
        return JobPerformanceModel.query.get(performance_id)


    @staticmethod
    def get_all():
        return JobPerformanceModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_job_performance(job_performance, data):
        for key, value in data.items():
            setattr(job_performance, key, value)
        db.session.commit()
        return job_performance

    @staticmethod
    def delete_job_performance(job_performance):
        job_performance.deleted_at = datetime.utcnow()
        db.session.commit()