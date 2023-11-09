import logging
import json

from celery import shared_task
from django.core import serializers

from src.models import File
from celery_app import app


@shared_task
def update_process_file(file_id):
    try:
        file = File.objects.get(id=file_id)
        file.processed = True
        file.save()
        return serializers.serialize("json", [file, ])[33: -2]
    except File.DoesNotExist:
        logging.error(f"Файл с id {file_id} не найден.")
        return {"message": "Запись не найдена!"}

