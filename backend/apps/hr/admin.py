from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_code','full_name','phone','hire_date','is_active')
    search_fields = ('employee_code','full_name','national_id')
