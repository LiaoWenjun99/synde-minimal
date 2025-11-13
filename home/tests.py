from django.db import models

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ("esmfold", "ESMFold structure prediction"),
        ("other", "Other model"),
    ]

    job_type = models.CharField(max_length=32, choices=JOB_TYPE_CHOICES)
    status = models.CharField(
        max_length=16,
        default="PENDING",
        choices=[
            ("PENDING", "PENDING"),
            ("RUNNING", "RUNNING"),
            ("SUCCESS", "SUCCESS"),
            ("FAILURE", "FAILURE"),
        ],
    )
    input_sequence = models.TextField()
    result_path = models.TextField(blank=True, null=True)   # e.g. PDB path or S3 URL
    result_json = models.JSONField(blank=True, null=True)   # metrics, scores, etc.
    error_message = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job_type} #{self.id} [{self.status}]"
