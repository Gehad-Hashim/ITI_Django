from django.urls import path
from  staff.views import *

urlpatterns = [
    path('list/',addClassStaff,name='addStaff')
]