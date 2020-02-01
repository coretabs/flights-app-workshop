from django.contrib import admin
from .models import Plane, Flight, Passenger, Ticket, User_Info 
# Register your models here.
admin.site.register(Plane)
admin.site.register(Passenger)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(User_Info)