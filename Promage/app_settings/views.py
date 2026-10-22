from rest_framework import viewsets

from .models import AppSetting
from .serializers import AppSettingSerializer


class AppSettingViewSet(viewsets.ModelViewSet):
    queryset = AppSetting.objects.all()
    serializer_class = AppSettingSerializer
    lookup_field = "key"
