from flask import abort, jsonify
from flask_smorest import Blueprint
from app.repository.job_performance_repo import JobPerformanceRepository
from app.schema.job_performance_schema import JobPerformanceSchema

job_performance_blp = Blueprint('job_performance', 'job_performance', url_prefix='/job_performance', description="Operation for job performance")


@job_performance_blp.route("/", methods=['POST'])
@job_performance_blp.arguments(JobPerformanceSchema)
@job_performance_blp.response(201, JobPerformanceSchema)
def create_job_performance(data):
    job_performance = JobPerformanceRepository.create_job_performance(data)
    return job_performance


@job_performance_blp.route("/<string:user_id>", methods=['GET'])
@job_performance_blp.response(200, JobPerformanceSchema)
def get_job_performance_by_id(performance_id):
    job_performance = JobPerformanceRepository.get_job_performance_by_id(performance_id)
    if not job_performance:
        return jsonify({"message": "not found"}), 404
    return job_performance


@job_performance_blp.route("/", methods=['GET'])
@job_performance_blp.response(200, JobPerformanceSchema(many=True))
def get_all_job_performance():
    job_performance = JobPerformanceRepository.get_all()
    return job_performance


@job_performance_blp.route("/<string:user_id>", methods=['PUT'])
@job_performance_blp.arguments(JobPerformanceSchema)
@job_performance_blp.response(200, JobPerformanceSchema)
def update_job_performance(data, performance_id):
    job_performance = JobPerformanceRepository.get_job_performance_by_id(performance_id)
    if not job_performance:
        abort(description="Job performance not found"), 404
    updated_job_performance = JobPerformanceRepository.update_job_performance(job_performance, data)
    return updated_job_performance


@job_performance_blp.route("/<string:user_id>", methods=['DELETE'])
@job_performance_blp.response(204)
def delete_job_performance(performance_id):
    job_performance = JobPerformanceRepository.get_job_performance_by_id(performance_id)

    if not job_performance:
        abort(description="Job performance Not Found"), 404
    JobPerformanceRepository.delete_job_performance(job_performance)
    return ''