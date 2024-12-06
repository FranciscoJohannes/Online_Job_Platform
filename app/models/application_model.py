
from app.extension import db


class ApplicationModel(db.Model):
    __tablename__ = 'application'

    application_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_seeker_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    job_id = db.Column(db.Integer, db.ForeignKey('job_posting.job_id'))
    resume = db.Column(db.LargeBinary, nullable=False)
    status = db.Column(db.Enum('user'), nullable=False)
    skills = db.Column(db.Text(255), nullable=False)
    work_experience = db.Column(db.Text(255), nullable=False)
    applied_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

