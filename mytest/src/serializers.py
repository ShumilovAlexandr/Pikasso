from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import File
from .tasks import process_file


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ["file", "uploaded_at", "file_size", "file_type"]

    file_size = serializers.SerializerMethodField()
    file_type = serializers.SerializerMethodField()

    def get_file_size(self, obj):
        return obj.file.size

    def get_file_type(self, obj):
        return obj.file.name.split(".")[-1]

    def create(self, validated_data):
        # file = validated_data.pop('file')
        # uploaded_at = validated_data.pop('uploaded_at')
        # processed = process_file.delay()
        pass
