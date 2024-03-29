from django.urls import path
from . import views


urlpatterns = [
   path('', views.m3activity1, name = "m3activity1"),
   path('configItem', views.configItem, name = "configItem"),
   path('addItem', views.addItem, name = "addItem"),
   path('updateItem/<int:pk>/', views.updateItem, name = "updateItem"),
   path('deleteItem/<int:pk>/', views.deleteItem, name = "deleteItem"),
   path('confirmOrder', views.confirmOrder, name = "confirmOrder"),
   path('checkOrder', views.checkOrder, name = "checkOrder")
]
