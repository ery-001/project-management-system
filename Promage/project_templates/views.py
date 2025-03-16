from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import ProjectTemplate
from .serializers import ProjectTemplateSerializer


class ProjectTemplateViewSet(viewsets.ModelViewSet):
    queryset = ProjectTemplate.objects.all
    serializer_class = ProjectTemplateSerializer