from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path("", views.index, name='home'),
    path("register", views.register, name='register'),
    path("login", views.loginuser, name='login'),
    path("logout", views.logoutuser, name='logout'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contect", views.contect, name='contect'),
   

    
]