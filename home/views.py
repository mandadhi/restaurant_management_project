from django.shortcuts import render
from django.conf import settings

def home(request):
    restaraunt_name=settings.RESTARAUNT_NAME
    return render(request,'restaraunt_home.html',{'restaraunt_name':restaraunt_name})
# Create your views here.
