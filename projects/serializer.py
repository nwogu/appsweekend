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
        fields = ("id", "title", "description", "link", "status", "tasks", "tags")
