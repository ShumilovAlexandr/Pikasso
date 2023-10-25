# Generated by Django 4.2.6 on 2023-10-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_alter_file_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='processed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='static/files', verbose_name='Выбери файл'),
        ),
    ]
