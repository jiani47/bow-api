from rest_framework import serializers
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
        