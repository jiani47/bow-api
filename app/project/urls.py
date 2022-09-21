"""
URL mappings for the project API
"""
from django.urls import path
from project import views

app_name = 'project' #this is required so that employee is a registered namespace 

urlpatterns = [
    path('create/', views.CreateProjectView.as_view(), name='create'),
    path('', views.ListProjectView.as_view(), name='list')
]