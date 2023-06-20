import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_challenge_dev.settings")

broker_url = "amqp://guest@rabbitmq:5672//"
app = Celery("_challenge_dev")


app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
