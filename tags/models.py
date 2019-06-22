from django.db import models
from projects.models import Project

# Create your models here.

class Tag(models.Model):

    title = models.CharField(max_length=255)

    colour = models.CharField(max_length=255, blank=True)

    projects = models.ManyToManyField(Project, related_name="tags")

    def __str__(self):

        return self.title
