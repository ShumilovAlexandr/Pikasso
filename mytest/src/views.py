from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import FileSerializer
from .models import File


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


