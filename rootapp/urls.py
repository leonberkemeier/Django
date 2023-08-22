from turtle import home
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('camera', views.camera, name="camera"),
    path('rootapp', views.rootapp, name="rootapp"),
    path('', views.home, name="home"),
    path('home', views.home, name="home"),


]