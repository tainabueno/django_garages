from django.contrib import admin
from garage.models import Vehicle, Garage
from garage.forms import GarageForm

class VehiclesAdmin(admin.ModelAdmin):
    pass


class GarageAdmin(admin.ModelAdmin):
    form = GarageForm


admin.site.register(Vehicle, VehiclesAdmin)
admin.site.register(Garage, GarageAdmin)
