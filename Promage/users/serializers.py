from rest_framework import serializers
from authentication.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'profile_picture', 'position',]  # 🔥 Remove 'user' if it's here
