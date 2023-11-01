from rest_framework.generics import (CreateAPIView,
                                     ListAPIView)

from .serializers import (FileSerializer,
                          FileListSerializer)
from .models import File


class FileViewSet(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileListViewSet(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileListSerializer

