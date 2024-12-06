import uuid
from sqlalchemy.dialects.mysql import CHAR
from app.extension import db


class JobPostingTableModel(db.Model):
    __tablename__ = 'job_posting'

    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employer_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    job_title = db.Column(db.String(255), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    industry = db.Column(db.String(255), nullable=False)
    min_salary = db.Column(db.Numeric(precision=10, scale=2), nullable=True)
    max_salary = db.Column(db.Numeric(precision=10, scale=2), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)