from django.contrib import admin
from .models import  Department, Employee

admin.site.site_title = 'Employee & Department'
admin.site.site_header = 'Admin'

class DepartmentAdmin(admin.ModelAdmin):
	list_display = [
        'DeptCode', 
        'DeptName'
        ]

class EmployeeAdmin(admin.ModelAdmin):
	list_display = [
        'EmpNo', 
        'FName',
        'LName',
        'Sex',
        'Salary',
        'DeptCode'
        ]

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)