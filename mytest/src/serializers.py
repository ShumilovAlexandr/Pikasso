from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import File
from .tasks import update_process_file


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        # fields = ["id", "file", "uploaded_at", "file_size", "file_type"]
        fields = ["id", "file", "uploaded_at"]

    # file_size = serializers.SerializerMethodField()
    # file_type = serializers.SerializerMethodField()
    #
    # def get_file_size(self, obj):
    #     return obj.file.size
    #
    # def get_file_type(self, obj):
    #     return obj.file.name.split(".")[-1]


class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["id", "file", "uploaded_at", "processed", "id"]

