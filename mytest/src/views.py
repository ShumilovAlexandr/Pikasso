from rest_framework import viewsets

from .serializers import FileSerializer
from .models import File


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


