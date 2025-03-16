from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    manager = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    due_date = models.DateField()
    status_choices = [("ongoing", "Ongoing"), ("completed", "Completed"), ("delayed", "Delayed")]
    status = models.CharField(max_length=20, choices=status_choices, default="ongoing")
    progress = models.IntegerField(default=0)  # Percentage

    def __str__(self):
        return self.name
