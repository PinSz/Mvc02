from django.db import models

class Department(models.Model):
	DeptCode = models.CharField(max_length=2, blank=False)
	DeptName = models.CharField(max_length=20)

	def __str__(self):
		return self.DeptCode

class Employee(models.Model):
	EmpNo = models.CharField(max_length=3, default='',blank=False)
	FName = models.CharField(max_length=20, blank=False)
	LName = models.CharField(max_length=20, blank=False)
	SEX_CHOICES = [('M','Male'), ('F', 'Female')]
	Sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
	Salary = models.IntegerField(default=0)
	StartDate = models.DateField(blank=True)
	DeptCode = models.ForeignKey(Department, db_column='DeptCode_DeptCode', db_index=True)
	published = models.BooleanField(default=True)

	def __str__(self):
		return self.EmpNo


