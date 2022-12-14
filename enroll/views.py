from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration, StudentCourseRegistration
from .models import *
from django.contrib import messages
from django.db import transaction
from .sqltransactions import SQLDBTransactions

# Create your views here.

#This function adds a new Student
def add_show(request):
    stud = User.objects.all()
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            with transaction.atomic():
                nm = fm.cleaned_data['name']
                em = fm.cleaned_data['email']
                pw = fm.cleaned_data['password']
                reg = User(name=nm, email=em, password=pw)
                reg.save()
                fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu': stud})

#This function updates a Student's details
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updateStudent.html', {'form': fm})

#This function deletes a Student

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# if student is registered add student to course else throw error

def add_to_course(request):
    transactions = SQLDBTransactions()
    stud_course = Course.objects.all()
    if request.method == 'POST':
        nfm = StudentCourseRegistration(request.POST)
        mydata = User.objects.values_list('email')
        email_list = [e[0] for e in (list(mydata))]
        if nfm.is_valid():
            with transaction.atomic():
                nnm = nfm.cleaned_data['name_course']
                nem = nfm.cleaned_data['email_course']
                npw = nfm.cleaned_data['password_course']
                if nem in email_list:
                    nreg = Course(name_course=nnm, email_course=nem, password_course=npw)
                    nreg.save()
                    transactions.commit()
                    messages.success(request,"Student Added to Course Successfully")
                else:
                    transactions.rollback()
                    messages.success(request, "Register Student with a Valid Email first")
                nfm = StudentCourseRegistration()
    else:
        nfm = StudentCourseRegistration()
    return render(request, 'enroll/addtocourse.html', {'nform': nfm, 'stureg': stud_course})



