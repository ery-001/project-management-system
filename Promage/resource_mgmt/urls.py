from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResourceViewSet

router = DefaultRouter()
router.register(r'', ResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
