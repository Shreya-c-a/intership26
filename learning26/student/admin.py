from django.contrib import admin
from .models import Student, Product,cart,StudentProfile,service,category,department,subject,college,userprofile

# Register your models here.
admin.site.register(Student)
admin.site.register(Product)
admin.site.register(cart)
admin.site.register(StudentProfile)
admin.site.register(service)
admin.site.register(category)
admin.site.register(department)
admin.site.register(subject)
admin.site.register(college)
admin.site.register(userprofile)