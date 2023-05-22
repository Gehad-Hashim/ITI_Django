from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
# Create your views here.
def mainView(req):
    # return HttpResponse('hello world')
    return render(req,'homePage.html')


def list(req):
    students=student.objects.all()
    return render(req,'student/listStudents.html',{'stu':students})

def insert(req):
    return render(req,'insert.html')

def update(req):
    return render(req,'update.html')

def delete(req):
    return HttpResponseRedirect('list')