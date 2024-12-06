from flask import abort, jsonify
from flask_smorest import Blueprint
from app.repository.job_posting_repo import JobPostingRepository
from app.schema.job_posting_schema import JobPostingSchema

job_posting_blp = Blueprint('job_posting', 'job_posting', url_prefix='/job_posting', description="Operation for job posting")


@job_posting_blp.route("/", methods=['POST'])
@job_posting_blp.arguments(JobPostingSchema)
@job_posting_blp.response(201, JobPostingSchema)
def create_job_posting(data):
    job_posting = JobPostingRepository.create_job_posting(data)
    return job_posting


@job_posting_blp.route("/<string:user_id>", methods=['GET'])
@job_posting_blp.response(200, JobPostingSchema)
def get_job_posting_by_id(job_id):
    job_posting = JobPostingRepository.get_job_posting_by_id(job_id)
    if not job_posting:
        return jsonify({"message": "not found"}), 404
    return job_posting


@job_posting_blp.route("/", methods=['GET'])
@job_posting_blp.response(200, JobPostingSchema(many=True))
def get_all_job_posting():
    job_posting = JobPostingRepository.get_all()
    return job_posting


@job_posting_blp.route("/<string:user_id>", methods=['PUT'])
@job_posting_blp.arguments(JobPostingSchema)
@job_posting_blp.response(200, JobPostingSchema)
def update_job_posting(data, job_id):
    job_posting = JobPostingRepository.get_job_posting_by_id(job_id)
    if not job_posting:
        abort(description="User not found"), 404
    updated_job_posting = JobPostingRepository.update_job_posting(job_posting, data)
    return updated_job_posting


@job_posting_blp.route("/<string:user_id>", methods=['DELETE'])
@job_posting_blp.response(204)
def delete_job_posting(job_id):
    job_posting = JobPostingRepository.get_job_posting_by_id(job_id)

    if not job_posting:
        abort(description="Job posting Not Found"), 404
    JobPostingRepository.delete_job_posting(job_posting)
    return ''