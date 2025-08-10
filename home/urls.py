from django.urls import path
from django.conf.urls import handler404
from . import views
from .views import custom_404

handler404=custom_404
urlpatterns = [
    path('home',views.home),
    path('about',views.about,name='about'),
    
]