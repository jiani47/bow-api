"""
URL mappings for the Employee API
"""
from django.urls import path, include
from rest_framework import routers 
from employee import views

app_name = 'employee' #this is required so that employee is a registered namespace 

router = routers.DefaultRouter()
router.register(r'employee', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls))
]