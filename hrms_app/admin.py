from django.contrib import admin
from .models import *

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['emp_code','name','email','password','department','file','mobile_number','gender','birth_date','country','state','pincode','start_date','end_date','type','reason']

# class LeaveAdmin(admin.ModelAdmin):
#     list_display = ['ecode','start_date','end_date','number_days','type','reason']

admin.site.register(Emp, EmpAdmin)
# admin.site.register(Leave, LeaveAdmin)