from rest_framework import serializers
from app.project.models import Assignment
from core.models import models as core_models
from project.models import Project

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id','name', 'desc', 'priority', 'status', 
            'target_delivery_date', 'estimated_delivery_date',
            'actual_delivery_date'
        ]
        read_only_fields = ['id']
        
class ProjectAssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = [
            'id', 'project', 'employee', 'start_date', 'end_date'
        ]
        read_only_fields = ['id']