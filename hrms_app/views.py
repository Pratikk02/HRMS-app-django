import os
from django.conf import settings
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


# Create your views here.

def login(request):
    return render(request, 'login.html')


def check(request):
    ecode = request.POST.get('emp_code')
    pw = request.POST.get('password')
    data = Emp.objects.get(emp_code=ecode)
    context = {'data': data}
    if (Emp.objects.filter(emp_code=ecode, password=pw).exists()):
        request.session['ecode'] = ecode
        messages.success(request, "Logged in!")
        return render(request,'home.html', context)
    else:
        messages.warning(request, 'Please enter valid credentials!' )
    return redirect('login')

def register(request):
    return render(request, 'register.html')

def create_new(request):
    if request.method == 'POST':
        ecode = request.POST.get('empcode')
        name = request.POST.get('name')
        em = request.POST.get('email')
        bday = request.POST.get('birthdt')
        mob = request.POST.get('mobile')
        gen = request.POST.get('gender')
        dept = request.POST.get('dept')
        ctry = request.POST.get('country')
        st = request.POST.get('state')
        pin = request.POST.get('pincode')
        pwd = request.POST.get('password')
        repw = request.POST.get('re_password')

        employee = Emp(emp_code=ecode, name=name, email=em, birth_date=bday, mobile_number=mob, gender=gen,  department=dept, country=ctry, state=st, pincode=pin, password=pwd)
        if (Emp.objects.filter(emp_code=ecode).exists()):
            messages.info(request, 'Account already exists!')
            return redirect('login')
        elif (pwd!=repw):
            messages.info(request, 'Password are not same!')
            return redirect('register')
        elif (Emp.objects.filter(name=name, birth_date=bday).exists()):
            messages.info(request,'Already a Registered Employee')
            return redirect('register')
        else:
            employee.save()
            messages.info(request, 'New Account created! ')
            return redirect('login')

@login_required(login_url='login')
def home(request):
    ecode = request.session.get('ecode')
    data = Emp.objects.get(emp_code=ecode)
    st = datetime.strptime(str(data.start_date), "%Y-%m-%d") 
    en = datetime.strptime(str(data.end_date), "%Y-%m-%d")    
    start_date_date_only = st.date()
    end_date_date_only = en.date()
    date_difference = end_date_date_only - start_date_date_only
    days = date_difference.days
    context = {'data': data,
               'days': days}
    return render(request, "home.html", context)


@login_required(login_url='login')
def logout(request):
    return redirect('login')

@login_required(login_url='login')
def emp_detail(request):
    emp_code = request.session.get('ecode')
    print(emp_code)
    data = Emp.objects.get(emp_code=emp_code)
    context = {'data': data}
    return render(request,'emp_detail.html',context)

@login_required(login_url='login')
def master_list(request):
    ecode = request.session.get('ecode')
    emp = Emp.objects.get(emp_code=ecode)
    data = Emp.objects.all()
    context = {'data': data,
               'emp': emp}
    return render(request, "master_list.html", context)

@login_required(login_url='login')
def leave(request):
    ecode = request.session.get('ecode')
    data = Emp.objects.get(emp_code=ecode)
    st = datetime.strptime(str(data.start_date), "%Y-%m-%d") 
    en = datetime.strptime(str(data.end_date), "%Y-%m-%d")    
    start_date_date_only = st.date()
    end_date_date_only = en.date()
    date_difference = end_date_date_only - start_date_date_only
    days = date_difference.days
    context = {'data': data,
               'days': days}
    messages.info(request, 'One can only take 1 Leave in one Month..!')
    return render(request, 'leave.html',context)    

@login_required(login_url='login')
def change_pass(request):
    ecode = request.session.get('ecode')
    data = Emp.objects.get(emp_code=ecode)
    context = {'data': data}
    return render(request, 'change_pass.html',context)

@login_required(login_url='login')
def change(request):
    ecode = request.session.get('ecode')
    opwd = request.POST.get('opws')
    npwd = request.POST.get('npws')
    repwd = request.POST.get('repws')
    emp = Emp.objects.get(emp_code=ecode)

    if emp.password==opwd:
        if opwd!=npwd:
            if npwd==repwd:
                # data = Emp(password=npwd)
                Emp.objects.filter(emp_code=ecode).update(password=npwd)
                # data.save()
                messages.success(request, 'Password Changed Successfully..!!')
                return redirect('home')
            else:
                messages.info(request, "Entered Passwords are not Same..!")
                return redirect('change_pass')
        else:
            messages.info(request, 'Old and New Password cannot be Same..!')
    else:
        messages.info(request, 'Invalid Old Password..!')
        return redirect('change_pass')

@login_required(login_url='login')
def upload(request):
    ecode = request.session.get('ecode')
    data = Emp.objects.get(emp_code=ecode)
    context = {'data': data}
    return render(request,'upload.html', context)


@login_required(login_url='login')
def fupload(request):
    ecode = request.session.get('ecode')
    data = Emp.objects.get(emp_code=ecode)

    if request.method == "POST":
        files = request.FILES.getlist('fn')
        if files:
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'uploads', ecode))

            for file in files:
                data.file = file
                data.save()
                
                fs.save(file.name, file)

            messages.success(request, "Files uploaded successfully!")

            return redirect('upload')
    else:
        messages.error(request, 'Not logged in..!')
        return redirect('login')
    

@login_required(login_url='login')
def ileave(request):
    ecode = request.session.get('ecode')
    data = Emp.objects.get(emp_code=ecode)
    context = {'data': data}
    return render(request,'ileave.html', context)

@login_required(login_url='login')
def issue(request):
    ecode = request.session.get('ecode')
    data = Emp.objects.get(emp_code=ecode)
    if request.method == "POST":
        st = request.POST.get('start-date')
        ed = request.POST.get('end-date')
        tp = request.POST.get('leave-type')
        re = request.POST.get('reason')

        data.start_date = st
        data.end_date = ed
        data.type = tp
        data.reason = re
        data.save()
        # data = Emp(start_date=st, end_date=ed, type=type, reason=re)
        messages.success(request, 'Leave Applied..!')
        return redirect('leave')
    