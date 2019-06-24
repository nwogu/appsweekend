from rest_framework import serializers
from .models import Project
from tasks.models import Task
from tags.serializer import TagSerializer
from tasks.serializer import TaskSerializer

class ProjectSerializer(serializers.ModelSerializer):

    tasks = TaskSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            "id", "title", "description", "image_url"
            "app_link", "status", "tasks", "tags", 
            "blog_link", "frontend_github_link",
            "backend_github_link", "created", "updated")
