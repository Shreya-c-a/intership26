from . import views
from django.urls import path
urlpatterns = [
    path('employeeList/', views.employeeList),
    path('employeeFilter/', views.employeeFilter),
    path('createEmployee/', views.createEmployee),
    path('createEmployeeWithForm/',views.createEmployeeWithForm),
    path('createcours/',views.createcours),
    path('createlibrary/',views.createlibrary),
    path('createevent/',views.createevent),
]