class ProjectTemplateSerializer(serializers.ModelSerializer):
    class  Meta:
        model = ProjectTemplate
        fields = "__all__"



from rest_framework import serializers
from .models import ProjectTemplate