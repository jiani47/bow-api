

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from app.project.models import Assignment
from app.project.serializers import ProjectAssignmentSerializer

from project.serializers import ProjectSerializer
from project.models import Project

class CreateProjectView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ListProjectView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().order_by('-id')
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ListProjectAssignmentsView(generics.ListAPIView):
    serializer_class = ProjectAssignmentSerializer
    queryset = Assignment.objects.all().order_by('project')
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class CreateProjectAssignmentView(generics.CreateAPIView):
    pass

class UpdateProjectAssignmentView(generics.UpdateAPIView):
    pass

class DeleteProjectAssignementView(generics.DestroyAPIView):
    pass