from django.contrib import admin
from django.urls import path, re_path, include
from apps.core import views

urlpatterns = [
    path('', views.home , name='home'),
    path('control/horario', views.control , name='control'),
    path('recreacion', views.recreacion , name='recreacion'),
]