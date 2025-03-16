from django.db import models
from django.conf import settings
from django.core.mail import send_mail

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='projects')

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assigned_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")  # ✅ Added Status Field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.status}"

    def save(self, *args, **kwargs):
        
        # Send email notification when a new task is assigned
        if not self.pk:  # Only send email on task creation
            send_mail(
                subject="New Task Assigned",
                message=f"Hello {self.assigned_user.username},\n\n"
                        f"You have been assigned a new task: {self.title}.\n"
                        f"Project: {self.project.name}\n"
                        f"Due Date: {self.due_date}\n\n"
                        f"Please check your dashboard for details.",
                from_email="admin@example.com",
                recipient_list=[self.assigned_user.email],
                fail_silently=True,
            )
        super().save(*args, **kwargs)


from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def send_task_update(task):
    """Send real-time updates when a task status changes."""
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "tasks_updates",
        {
            "type": "task_update",
            "message": {
                "task_id": task.id,
                "status": task.status,
                "assigned_user": task.assigned_user.username,
                "project": task.project.name,
            },
        },
    )
