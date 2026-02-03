from django.urls import path
from .import views
urlpatterns = [
    path('details/', views.studentdetails),
    path('marks/', views.studentmarks),
    path('attendance/', views.studentattendance),   
    path('fees/', views.studentfees),
    
]