from django.db import models

# Create your models here.
class DashboardStats(models.Model):
    total_revenue = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    total_projects = models.IntegerField(default=0)
    total_hours = models.IntegerField(default=0)
    total_resources = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True,)

    # def __str__(self):
    #     return f"Dass"

    def __str__(self):
        return f"Dashboard Stats - {self.updated_at}"
