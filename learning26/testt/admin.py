from django.contrib import admin
from .models import User, Admin, ParkingLot, ParkingSlot, Reservation, Payment, Notification, Analytics
# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(ParkingLot)
admin.site.register(ParkingSlot)
admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Notification)
admin.site.register(Analytics)