from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from employee.models import Employee

EMPLOYEE_URL = reverse('employee:employee-list')
class EmployeeTests(TestCase):
    def setUp(self):
        self.superuser_client = APIClient()
        self.superuser = get_user_model().objects.create_superuser(
            'admin@example.com',
            'testpassword123'
        )
        self.superuser_client.force_authenticate(user=self.superuser)
        self.regularuser = get_user_model().objects.create_user(
            'sam@example.com',
            'samisawesome123'
        )
        self.regularuser_client = APIClient()
        self.regularuser_client.force_authenticate(user=self.regularuser)

    def create_employee_in_db(self, full_name):
        payload = {
            'full_name' : full_name
        }
        return Employee.objects.create(**payload)


    def test_employee_model(self):
        payload = {
            'full_name' : 'Jia Ni'
        }
        employee = Employee.objects.create(**payload)
        self.assertEqual(employee.full_name, payload['full_name'])

    def test_create_employee_successfully_for_admin(self):
        payload = {
            'full_name' : 'Jia Ni'
        }
        res = self.superuser_client.post(EMPLOYEE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        employee = Employee.objects.get(id=res.data['id'])
        self.assertEqual(employee.full_name, payload['full_name'])

    def test_create_employee_failed_for_non_admin(self):
        payload = {
            'full_name' : 'Jia Ni'
        }
        res = self.regularuser_client.post(EMPLOYEE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_all_employees(self):
        e1 = self.create_employee_in_db('Jia Ni')
        e2 = self.create_employee_in_db('Kejun Sun')
        res = self.superuser_client.get(EMPLOYEE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
        # verify sorted in full name ascending order
        self.assertEqual(res.data[0]['full_name'], e1.full_name)
        self.assertEqual(res.data[1]['full_name'], e2.full_name)
