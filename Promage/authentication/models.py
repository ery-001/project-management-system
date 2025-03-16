from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role_choices = [("admin", "Admin"), ("manager", "Manager"), ("employee", "Employee")]
    role = models.CharField(max_length=20, choices=role_choices, default="employee")
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)

    def __str__(self):
        return self.username
