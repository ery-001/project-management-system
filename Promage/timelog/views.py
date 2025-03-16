from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import TimeLog
from .serializers import TimeLogSerializer

class TimeLogViewSet(viewsets.ModelViewSet):
    queryset = TimeLog.objects.all()
    serializer_class = TimeLogSerializer
    permission_classes = [permissions.IsAuthenticated]
