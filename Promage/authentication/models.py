from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    role_choices = [
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("employee", "Employee")
    ]
    
    role = models.CharField(max_length=20, choices=role_choices, default="employee")
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)  # 🔥 Add this if you need it

    def __str__(self):
        return self.username
