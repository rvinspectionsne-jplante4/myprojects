from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('motor_a/', views.motor_a, name='Class A'),
    path('motor_b/', views.motor_b, name='Class B/B+'),
    path('motor_c/', views.motor_c, name='Class C'),
    path('bumper_pull/', views.bumper_pull, name='Travel Trailer'),
    path('fiver/', views.fiver, name='Fifth Wheel'),
    path('training/', views.training, name='Training'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='Contact'),
    path('success/', views.success, name='Success'),
   ]

