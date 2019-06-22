from .models import Project
from django.shortcuts import render
from rest_framework import generics
from .serializer import ProjectSerializer

# Create your views here.

class ProjectListActive(generics.ListAPIView):
    
    queryset = Project.objects.filter(status="active")

    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveAPIView):

    queryset = Project.objects.all()

    serializer_class = ProjectSerializer

class ProjectListCompleted(generics.ListAPIView):

    queryset = Project.objects.filter(status="completed")

    serializer_class = ProjectSerializer

class ProjectList(generics.ListAPIView):

    queryset = Project.objects.all()

    serializer_class = ProjectSerializer