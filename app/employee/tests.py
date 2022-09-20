from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from employee.models import Employee

CREATE_EMPLOYEE_URL = reverse('employee:employee-list')
class EmployeeTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.superuser = get_user_model().objects.create_superuser(
            'admin@example.com',
            'testpassword123'
        )
        self.client.force_authenticate(user=self.superuser)

    def test_employee_model(self):
        payload = {
            'full_name' : 'Jia Ni'
        }
        employee = Employee.objects.create(**payload)
        self.assertEqual(employee.full_name, payload['full_name'])

    def test_create_employee_successfully_only_for_admin(self):
        payload = {
            'full_name' : 'Jia Ni'
        }
        res = self.client.post(CREATE_EMPLOYEE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        employee = Employee.objects.get(id=res.data['id'])
        self.assertEqual(employee.full_name, payload['full_name'])
