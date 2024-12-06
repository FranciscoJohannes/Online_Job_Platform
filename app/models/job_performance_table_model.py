
from app.extension import db


class JobPerformanceModel(db.Model):
    __tablename__ = 'job_performance'

    performance_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job_posting.job_id'))
    applications_count = db.Column(db.Integer, nullable=False)
    views_count = db.Column(db.Integer, nullable=False)
    open_date = db.Column(db.DateTime, nullable=False)
    close_date = db.Column(db.DateTime, nullable=False)
    time_to_fill = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)