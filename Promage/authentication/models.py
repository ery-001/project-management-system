from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    role_choices = [
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("employee", "Employee")
    ]
    
    role = models.CharField(max_length=20, choices=role_choices, default="employee")
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_users",  # Fixes conflict with auth.User.groups
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_users_permissions",  # Fixes conflict with auth.User.user_permissions
        blank=True
    )

    def __str__(self):
        return self.username
