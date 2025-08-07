from django.shortcuts import render
from django.conf import settings

def home(request):
    restaraunt_name=settings.restaraunt_name
    return render(request,'homepage.html',{'restaraunt_name':restaraunt_name})
# Create your views here.
