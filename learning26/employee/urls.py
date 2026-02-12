from . import views
from django.urls import path
urlpatterns = [
    path('employeeList/', views.employeeList,name="employeeList"),
    path('employeeFilter/', views.employeeFilter),
    path('createEmployee/', views.createEmployee),
    path('createEmployeeWithForm/',views.createEmployeeWithForm,name="createEmployeeWithForm"),  
    path('createcours/',views.createcours),
    path('createlibrary/',views.createlibrary),
    path('createevent/',views.createevent),
    path("deleteEmployee/<int:id>",views.deleteEmployee,name="deleteEmployee"),
    path("filterEmployee/",views.filterEmployee,name="filterEmployee"),
    path("sortEmployee/<int:id>",views.sortEmployee,name="sortEmployee"),
]