from django.db import models
from django.contrib.auth.models import User


class License(models.Model):
    licence = models.CharField(max_length=16)
    validated = models.BooleanField()


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=15, null=True)
    date = models.DateField(null=True)
    GENDER_CHOICES = (('M', 'Male'),
                      ('F', 'Female'),)
    gender = models.CharField(max_length=50, null=True, choices=GENDER_CHOICES)
    DEPT_CHOICES = (('C', 'CEO'),
                    ('H', 'HR'),
                    ('S', 'SALES'),
                    ('A', 'ACCOUNTS'))
    dept = models.CharField(max_length=100, choices=DEPT_CHOICES)
    # position = models.CharField(max_length=50, null=True)
    date_of_joining = models.DateField(null=True)
    reporting_to = models.ForeignKey(
        "Employee", null=True, on_delete=models.CASCADE)
    is_verified = models.BooleanField()
    is_complete = models.BooleanField()
    cv = models.FileField(upload_to='Media/cv')
    profile_pic = models.ImageField(upload_to='Media/profile_pics')
