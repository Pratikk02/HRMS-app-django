from django.db import models
import datetime

class Emp(models.Model):
    emp_code = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=10)
    department = models.CharField(default= 'Trainee',max_length=50)
    mobile_number = models.IntegerField(null=True)
    gender = models.CharField(default=None, max_length=10)
    birth_date = models.DateField(default=datetime.date.today)
    country = models.CharField(default='India', max_length=100)
    state = models.CharField(default=None, max_length=100)
    pincode = models.IntegerField(default=None)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    type = models.CharField(null=True, blank=True, max_length=50)
    reason = models.CharField(null=True, blank=True, max_length=80)


# class Leave(models.Model):
#     ecode = models.ForeignKey(Emp, on_delete=models.CASCADE, to_field='emp_code')
#     start_date = models.DateField()
#     end_date = models.DateField()
#     number_days = models.PositiveIntegerField()
#     type = models.CharField(max_length=10, choices=[('full', 'Full'), ('half', 'Half')])
#     reason = models.TextField()

