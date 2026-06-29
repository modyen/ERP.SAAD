from django.test import TestCase
from .models import Employee

class EmployeeModelTest(TestCase):
    def test_create_employee(self):
        employee = Employee.objects.create(
            employee_code='EMP001',
            full_name='Test Employee',
            national_id='12345678901234',
            phone='01000000000',
            hire_date='2026-01-01'
        )
        self.assertEqual(employee.full_name, 'Test Employee')
