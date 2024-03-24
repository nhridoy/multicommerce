import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Celery Beat Settings
app.conf.beat_schedule = {
    "periodic_task": {
        "task": "ecommerce.tasks.daily_job",
        # "schedule": crontab(minute="*/1", hour="0", day_of_month='*', month_of_year="*", day_of_week="*"),
        "schedule": 10,
        # "args": {today - timedelta(days=1)},
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
