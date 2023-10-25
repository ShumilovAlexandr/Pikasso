from django.urls import include, path
from rest_framework import routers

from .views import FileViewSet


router = routers.DefaultRouter()
router.register('upload',
                FileViewSet,
                basename='upload_file')

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('upload/', FileViewSet.as_view(), name="upload_file"),
# ]
