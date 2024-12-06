import uuid
from sqlalchemy.dialects.mysql import CHAR
from app.extension import db


class UserModel(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    authentication_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    skills = db.Column(db.Text(255), nullable=False)
    work_experience = db.Column(db.Text(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)