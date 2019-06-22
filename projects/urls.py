from projects import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.ProjectList.as_view()),
    path("active", views.ProjectListActive.as_view()),
    path("completed", views.ProjectListCompleted.as_view()),
    path("<int:pk>", views.ProjectDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)