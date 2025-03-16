from django.db import models

# Create your models here.
class DashboardStats(models.Model):
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    total_projects = models.IntegerField()
    total_hours = models.IntegerField()
    total_resources = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"Dass"

    def __str__(self):
        return f"Dashboard Stats - {self.updated_at}"
