from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProjectTemplateViewSet

router = DefaultRouter()
router.register(r"", ProjectTemplateViewSet, basename="project-template")

urlpatterns = [
    path("", include(router.urls)),
]
