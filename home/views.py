from django.shortcuts import render
from django.conf import settings

def home(request):
    restaraunt_name=settings.RESTARAUNT_NAME
    return render(request,'restaraunt_home.html',{'restaraunt_name':restaraunt_name})
# Create your views here.
def custom_404(request,exception):
    return render(request,'page_404.html',status=404)
def about(request):
    return render(request,'Aboutus.html')
def contact(request):
    return render(request,'Contactus.html')