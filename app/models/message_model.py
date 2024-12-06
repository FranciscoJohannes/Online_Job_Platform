import uuid
from sqlalchemy.dialects.mysql import CHAR
from app.extension import db


class MessageModel(db.Model):
    __tablename__ = 'message'

    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer,  db.ForeignKey('user.user_id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    message_text = db.Column(db.String(255), nullable=False)
    is_read = db.Column(db.Enum('user', 'date'), nullable=False)
    message_type = db.Column(db.DateTime, nullable=False)
    sent_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)