from rest_framework.generics import (CreateAPIView,
                                     ListAPIView)
from rest_framework.response import Response
from rest_framework import status

from .serializers import (FileSerializer,
                          FileListSerializer)
from .models import File
from .tasks import update_process_file


class FileViewSet(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            update_process_file.delay(serializer.data["id"])
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)


class FileListViewSet(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileListSerializer


