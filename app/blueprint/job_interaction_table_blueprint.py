from flask import abort, jsonify
from flask_smorest import Blueprint
from app.repository.job_interaction_table_repo import JobInteractionTableRepository
from app.schema.job_interaction_table_schema import JobInteractionTableSchema

job_interaction_table_blp = Blueprint('job_interaction_table', 'job_interaction_table', url_prefix='/job_interaction_table', description="Operation for job interaction table")


@job_interaction_table_blp.route("/", methods=['POST'])
@job_interaction_table_blp.arguments(JobInteractionTableSchema)
@job_interaction_table_blp.response(201, JobInteractionTableSchema)
def create_job_interaction_table(data):
    job_interaction_table = JobInteractionTableRepository.create_job_interaction_table(data)
    return job_interaction_table


@job_interaction_table_blp.route("/<string:user_id>", methods=['GET'])
@job_interaction_table_blp.response(200, JobInteractionTableSchema)
def get_job_interaction_table_by_id(interaction_id):
    job_interaction_table = JobInteractionTableRepository.get_job_interaction_table_by_id(interaction_id)
    if not job_interaction_table:
        return jsonify({"message": "not found"}), 404
    return job_interaction_table


@job_interaction_table_blp.route("/", methods=['GET'])
@job_interaction_table_blp.response(200, JobInteractionTableSchema(many=True))
def get_job_interaction_table():
    job_interaction_table = JobInteractionTableRepository.get_all()
    return job_interaction_table


@job_interaction_table_blp.route("/<string:user_id>", methods=['PUT'])
@job_interaction_table_blp.arguments(JobInteractionTableSchema)
@job_interaction_table_blp.response(200, JobInteractionTableSchema)
def update_job_interaction_table(data, interaction_id):
    job_interaction_table = JobInteractionTableRepository.get_job_interaction_table_by_id(interaction_id)
    if not job_interaction_table:
        abort(description="Job interaction table not found"), 404
    updated_job_interaction_table = JobInteractionTableRepository.update_job_interaction_table(job_interaction_table, data)
    return updated_job_interaction_table


@job_interaction_table_blp.route("/<string:user_id>", methods=['DELETE'])
@job_interaction_table_blp.response(204)
def delete_job_interaction_table(interaction_id):
    job_interaction_table = JobInteractionTableRepository.get_job_interaction_table_by_id(interaction_id)

    if not job_interaction_table:
        abort(description="Job interaction table Not Found"), 404
    JobInteractionTableRepository.delete_job_interaction_table(job_interaction_table)
    return ''