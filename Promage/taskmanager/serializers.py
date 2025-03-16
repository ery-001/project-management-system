from rest_framework import serializers
from .models import Project, Task
from django.contrib.auth import get_user_model

User = get_user_model()
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        assigned_users = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username",  # Use username instead of ID
        many=True
    )

    class Meta:
        model = Project
        fields = ["id", "name", "description", "assigned_users"]
        read_only_fields = ['completed']  # Completed field is managed by status

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['completed']  # Completed field is managed by status
