from django.urls import path
from  .views import *

urlpatterns = [
    path('listStudent/',listStudent),
    path('listStaff',listStaff),
    path('mainReport',mainReport),
    # path('delete',delete)
]
