import datetime

from django.db import models


class File(models.Model):
    file = models.FileField(verbose_name='Выбери файл',
                            upload_to='static/files')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

