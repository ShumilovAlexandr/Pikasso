import os
import time

from celery import Celery


app = Celery("mytest")

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "mytest.settings")
app.config_from_object("django.conf:settings",
                       namespace="CELERY")

app.autodiscover_tasks()


