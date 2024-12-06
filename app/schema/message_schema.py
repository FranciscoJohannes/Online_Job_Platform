from marshmallow import Schema, fields


class MessageSchema(Schema):
    message_id = fields.Int(dump_only=True)
    sender_id = fields.Str(dump_only=True)
    recipient_id = fields.Str(dump_only=True)
    message_text = fields.Str(required=True)
    is_read = fields.Str(required=True)
    message_type = fields.Str(required=True)
    sent_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)