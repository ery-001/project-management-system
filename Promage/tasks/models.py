from django.db import models

# Create your models here.
class Task(models.Model):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255)
    assigned_to = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    priority_choices = [("low", "Low"), ("medium", "Medium"), ("high", "High")]
    priority = models.CharField(max_length=10, choices=priority_choices, default="medium")
    status_choices = [("approved", "Approved"), ("in_review", "In Review"), ("on_going", "Ongoing")]
    status = models.CharField(max_length=20, choices=status_choices, default="on_going")

    def __str__(self):
        return self.title
