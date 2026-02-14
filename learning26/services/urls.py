from django.urls import path
from . import views

urlpatterns = [
    path('', views.serviceList, name='servicelist'),
    path('create/', views.createService, name='servicecreate'),
    path('update/<int:id>/', views.updateService, name='serviceupdate'),
    path('delete/<int:id>/', views.deleteService, name='servicedelete'),
]