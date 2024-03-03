from django.urls import path
from . import views


urlpatterns = [
   path('', views.m3activity1, name = "m3activity1"),
]
