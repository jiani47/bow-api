"""
Serializer for Employee API
"""
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

from employee.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'full_name']
        read_only_fields = ['id']
        
    