from django.contrib import admin
from vehicles.models import *
# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle
    list_display = ['id','vehicle_number','vehicle_type','vehicle_model','vehicle_description']

admin.site.register(Vehicle,VehicleAdmin)