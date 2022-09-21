from django.test import TestCase
from django.contrib.auth import get_user_model
from project.models import Project
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from rest_framework import status

# Create your tests here.
CREATE_PROJECT_URL = reverse('project:create')
LIST_PROJECT_URL = reverse('project:list')

class TestProjectApi(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user('test@example.com', 'password123')
        self.client.force_authenticate(user=self.user)
    
    def create_project(self, name, desc, priority, status):
        payload = {
            'name' : name,
            'desc' : desc,
            'priority' : priority,
            'status' : status
        }
        return Project.objects.create(**payload)


    def test_project_creation_successful(self):
        payload = {
            'name' : 'Message Explorer',
            'desc' : 'Message Explorer Performance improvements',
            'priority' : 1,
            'status' : 'IN PROGRESS',
        }
        p = Project.objects.create(**payload)
        self.assertEqual(p.name, payload['name'])
        self.assertEqual(p.desc, payload['desc'])
        self.assertEqual(p.priority, payload['priority'])
        self.assertEqual(p.status, payload['status'])
        self.assertIsNone(p.target_delivery_date)
        self.assertIsNone(p.estimated_delivery_date)
        self.assertIsNone(p.actual_delivery_date)

    def test_create_project_via_api(self):
        payload = {
            "name": "string",
            "desc": "string",
            "priority": 0,
            "status": "string"
        }
        res = self.client.post(CREATE_PROJECT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], payload['name'])


    def test_list_projects_via_api(self):
        self.create_project('Flow Control V3', 'Flow Control v3', 2, 'DONE')
        self.create_project('Core API', 'Batchless sending', 1, 'IN PROGRESS')
        res = self.client.get(LIST_PROJECT_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
    

      