from django.db import models

# Create your models here.

class Project(models.Model):

    PROJECT_STATUS = (
        ("draft", "Draft"),
        ("active", "Active"),
        ("completed", "Completed")
    )

    title = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    image_url = models.CharField(max_length=255, blank=True)

    app_link = models.CharField(max_length=255, blank=True)

    blog_link = models.CharField(max_length=255, blank=True)

    frontend_github_link = models.CharField(max_length=255, blank=True)

    backend_github_link = models.CharField(max_length=255, blank=True)

    status = models.CharField(max_length=255, choices=PROJECT_STATUS, default="draft")

    created = models.DateTimeField(auto_now_add=True)
    
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        
        return self.title
