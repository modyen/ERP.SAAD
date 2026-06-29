from django.db import models


class Employee(models.Model):
    employee_code = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=200)
    national_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
