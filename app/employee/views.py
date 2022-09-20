"""
views for the Employee API
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from employee.serializers import EmployeeSerializer
from employee.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all().order_by('full_name')
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    