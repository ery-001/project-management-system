from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectTemplateViewSet


router = DefaultRouter()
router.register(r"". ProjectTemplateViewSet)


urlpatterns = router.urls
