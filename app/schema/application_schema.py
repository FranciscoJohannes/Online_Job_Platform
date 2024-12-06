from marshmallow import Schema, fields

class ApplicationSchema(Schema):
    application_id = fields.Int(dump_only=True)
    job_seeker_id = fields.Str(dump_only=True)
    job_id = fields.Str(dump_only=True)
    resume = fields.Str(required=True)
    status = fields.Int(required=True)
    skills = fields.DateTime(required=True)
    work_experience = fields.DateTime(required=True)
    applied_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
