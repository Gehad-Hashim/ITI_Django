from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

# Create your views here.
def list(req):
    res=HttpResponse('list all staffs')
    res.write('<br/><h4>welcome to our web site</h4><br/><h1> &copy;ITI-Open Source 2023<h1/>')
    return  res

def insert(req):
    return JsonResponse({"id":1,"name":"Gehad"})

def update(req):
    return JsonResponse({"id":1,"name":"Eng-Gehad"})

def delete(req):
    return HttpResponseRedirect('list')