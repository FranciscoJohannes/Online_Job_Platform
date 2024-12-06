from marshmallow import Schema, fields


class JobPostingSchema(Schema):
    job_id = fields.Int(dump_only=True)
    employer_id = fields.Str(dump_only=True)
    job_title = fields.Str(required=True)
    job_description = fields.Str(required=True)
    location = fields.Str(required=True)
    category = fields.Str(required=True)
    industry = fields.Str(required=True)
    min_salary = fields.Decimal(required=True)
    max_salary = fields.Decimal(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)


