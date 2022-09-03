from rest_framework import serializers
from core.models import models as core_models
from project.models import Project

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = []
        read_only_fields = []