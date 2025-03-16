from django.db import models

# Create your models here.
class TimeLog(models.Model):
    user = models.ForeignKey("authentication.CustomUser", on_delete=models.CASCADE)
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    hours_spent = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.project.name} - {self.hours_spent} hrs"
