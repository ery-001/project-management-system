from django.db import models

# Create your models here.
class Resource(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.project.name}"
