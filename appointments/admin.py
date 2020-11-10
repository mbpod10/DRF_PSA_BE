from django.contrib import admin
from .models import Appointment, Client, Trainer, AppointmentDay
# Register your models here.

admin.site.register(Appointment)
admin.site.register(Trainer)
admin.site.register(Client)
admin.site.register(AppointmentDay)
