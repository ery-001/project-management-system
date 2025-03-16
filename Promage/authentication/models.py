from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    role_choices = [
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("employee", "Employee")
    ]
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    
    role = models.CharField(max_length=20, choices=role_choices, default="employee")
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)  # 🔥 Add this if you need it
    phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=True)  # Adjust max_length as needed
    
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self): 
        return f"{self.username}: {self.phone_number}, {self.city}, {self.state} (Lat: {self.latitude}, Long: {self.longitude}"

