from ast import Pass
from django.contrib import admin

from .models import *

# Register your models here.
class BusAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("buses", )

admin.site.register(Station)
admin.site.register(Bus, BusAdmin)
admin.site.register(Passenger, PassengerAdmin)