from django.shortcuts import render

# Create your views here.
def studentdetails(request):
    student={"name":"john","age":22,"course":"python"}
    return render(request, 'student/studentdetails.html',student)
def studentmarks(request):
    marks={"name":"john","marks":95}
    return render(request, 'student/studentmarks.html',marks)
def studentattendance(request):
    attendance={"name":"john","attendance":88}
    return render(request, 'student/studentattendance.html',attendance)
def studentfees(request):
    fees={"name":"john","fees":50000}
    return render(request, 'student/studentfees.html',fees)