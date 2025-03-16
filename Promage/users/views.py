from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from .serializers import CustomUserSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]
