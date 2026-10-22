from rest_framework import serializers

from .models import AppSetting


class AppSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppSetting
        fields = ["id", "key", "value"]
