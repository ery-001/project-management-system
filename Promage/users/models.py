from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField("authentication.CustomUser", on_delete=models.CASCADE)
    position = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

