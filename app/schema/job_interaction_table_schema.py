from marshmallow import Schema, fields


class JobInteractionTableSchema(Schema):
    interaction_id = fields.Int(dump_only=True)
    user_id = fields.Str(dump_only=True)
    job_id = fields.Str(dump_only=True)
    interaction_type = fields.Str(required=True)
    interaction_date = fields.Str(required=True)
    is_applied = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)

