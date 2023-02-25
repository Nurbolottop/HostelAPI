from django.contrib import admin

from .models import Reservation,Rooms
# Register your models here.
admin.site.register(Rooms)
admin.site.register(Reservation)