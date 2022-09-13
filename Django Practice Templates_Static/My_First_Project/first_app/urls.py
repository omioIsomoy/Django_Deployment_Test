from django.urls import include, re_path
from django.urls import path
from first_app import views

urlpatterns = [

    path('index/', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),



]
