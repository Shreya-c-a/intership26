from django.contrib import admin
from .models import Employee,course,library,event

# Register your models here.
admin.site.register(Employee)
admin.site.register(course)
admin.site.register(library)
admin.site.register(event)
