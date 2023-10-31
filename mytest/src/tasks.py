from celery import shared_task
from rest_framework import status

from src.models import File
from celery_app import app


@app.task
def process_file(file_id):
    try:
        file = File.objects.get(id=file_id)
        file.processed = True
        file.save()
    except File.DoesNotExist:
        return {"message": "Файл не найден!"}

