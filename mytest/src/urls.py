from django.urls import (path,
                         include)

from .views import (FileViewSet,
                    FileListViewSet)


urlpatterns = [
    path('upload/', FileViewSet.as_view()),
    path('files/', FileListViewSet.as_view())
]
