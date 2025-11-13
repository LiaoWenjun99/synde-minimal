# home/tasks.py
import time
from celery import shared_task
from django.db import transaction
from .models import Job

@shared_task(bind=True, name="home.tasks.run_esmfold_job")
def run_esmfold_job(self, job_id: int):
    # Late import to avoid importing heavy models in Celery master if not needed
    from django.utils import timezone

    try:
        job = Job.objects.get(id=job_id)

        # Mark job as running
        job.status = "RUNNING"
        job.save(update_fields=["status", "updated_at"])

        # === TODO: plug in real ESMFold pipeline here ===
        # For now: simulate a long task
        time.sleep(10)

        # Example dummy result, replace with real file path / metrics
        job.result_json = {"dummy": "ok", "completed_at": timezone.now().isoformat()}
        job.status = "SUCCESS"
        job.save(update_fields=["status", "result_json", "updated_at"])

    except Exception as e:
        job = Job.objects.get(id=job_id)
        job.status = "FAILURE"
        job.error_message = str(e)
        job.save(update_fields=["status", "error_message", "updated_at"])
        raise
