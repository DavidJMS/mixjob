from django.contrib import admin
from django.urls import path, re_path, include
from apps.user import views

urlpatterns = [
    path('login/', views.login_to_plataform, name='login'),
]