from pathlib import Path
from models import Job, JobRun


def _run_job(job: Job) -> JobRun:
    pass


def _run_jobs(jobs: list[Job]) -> list[JobRun]:
    pass

def _load_jobs(path: Path) -> list[Job]:
    import yaml
    with open(path, "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def _log_job(job_run: JobRun) -> None:
    pass

def _log_jobs(job_runs: list[JobRun]) -> None:
    pass