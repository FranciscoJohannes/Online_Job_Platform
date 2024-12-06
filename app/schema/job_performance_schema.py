from marshmallow import Schema, fields


class JobPerformanceSchema(Schema):
    performance_id = fields.Int(dump_only=True)
    job_id = fields.Str(dump_only=True)
    applications_count = fields.Str(required=True)
    views_count = fields.Str(required=True)
    open_date = fields.Str(required=True)
    close_date = fields.Str(required=True)
    time_to_fill = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)


