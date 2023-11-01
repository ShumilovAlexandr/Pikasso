from celery import shared_task

from src.models import File


@shared_task
def update_process_file(file_id):
    try:
        file = File.objects.get(id=file_id)
        file.processed = True
        file.save()
        return True
    except File.DoesNotExist:
        return {"message": "Файл не найден!"}

