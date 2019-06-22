from django.db import models
from projects.models import Project

# Create your models here.

class Task(models.Model):

    title = models.CharField(max_length=255)

    status = models.BooleanField(default=False)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")

    class Meta:
        ordering = ("-status",)

    def __str__(self):
        
        return self.title
