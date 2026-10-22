from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AppSettingViewSet

router = DefaultRouter()
router.register(r"", AppSettingViewSet, basename="app-setting")

urlpatterns = [
    path("", include(router.urls)),
]
