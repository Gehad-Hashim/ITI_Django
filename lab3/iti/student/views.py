from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
# Create your views here.
#
# def list(req):
#     students=student.objects.all()
#     return render(req,'student/listStudents.html',{'stu':students})
#
# def insert(req):
#     return render(req,'student/insertNewStudent.html')