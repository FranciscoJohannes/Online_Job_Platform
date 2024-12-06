import uuid
from sqlalchemy.dialects.mysql import CHAR
from app.extension import db


class JobInteractionTableModel(db.Model):
    __tablename__ = 'job_interaction_table'

    interaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    job_id = db.Column(db.Integer, nullable=False)
    interaction_type = db.Column(db.String(255), nullable=False)
    interaction_date = db.Column(db.Enum('user', 'date'), nullable=False)
    is_applied = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)