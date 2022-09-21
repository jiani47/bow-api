"""
URL mappings for the Employee API
"""
from django.urls import path
from employee import views

app_name = 'employee' #this is required so that employee is a registered namespace 

urlpatterns = [
    path('create/', views.CreateEmployeeView.as_view(), name='create'),
    path('', views.ListEmployeeView.as_view(), name='list')
]