from marshmallow import Schema, fields


class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    authentication_id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    birth_date = fields.DateTime(required=True)
    skills = fields.Str(required=True, load_only=True)
    work_experience = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)