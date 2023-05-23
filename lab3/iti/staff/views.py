from django.shortcuts import render
from django.views import View
from  .models import staff
def addClassStaff(View):
    context={}
    context['name']='Gehad'
    def get(self,req):
        return  render(req,'staff/add.html',addClassStaff.context)

    def post(self,req):
        name=req.post['name']

        staff.objects.create(name=name)
        return  render(req,'staff/add.html',addClassStaff.context)
