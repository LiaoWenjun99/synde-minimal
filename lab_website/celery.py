# lab_website/celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab_website.settings")

app = Celery("lab_website")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
