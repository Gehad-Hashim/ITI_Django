from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def listStudent(req):
    return HttpResponse('<h1>here list All <span style="color:blue;font-weight:bold">Students</span></h1>')

def listStaff(req):
    return HttpResponse('<h1>here list All <span style="color:blue;font-weight:bold">Staff</span></h1>')

def mainReport(req):
    return HttpResponse('<a href="listStaff">click to list Staff</a><br/><a href="listStudent">click to list students</a>')