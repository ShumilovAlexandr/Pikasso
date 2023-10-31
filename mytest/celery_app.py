import os
import time

from django.conf import settings

from celery import Celery


app = Celery("mytest")

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "mytest.settings")
app.config_from_object("django.conf:settings",
                       namespace="CELERY")
app.conf.broker_url = settings.CELERY_BROKER_URL

app.autodiscover_tasks()


