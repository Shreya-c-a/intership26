from django import forms
from .models import Employee,course,library,event
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
class courseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = "__all__"
          # tamaro model name check karo

class libraryForm(forms.ModelForm):
    class Meta:
        model = library
        fields = "__all__"
class eventForm(forms.ModelForm):
    class Meta:
        model = event
        fields = "__all__"