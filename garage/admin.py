from django.contrib import admin
from garage.models import Vehicle, Garage
from garage.forms import GarageForm


class VehiclesAdmin(admin.ModelAdmin):
    pass


class VehiclesInline(admin.StackedInline):
    model = Vehicle


class GarageAdmin(admin.ModelAdmin):
    inlines = [VehiclesInline]


admin.site.register(Vehicle, VehiclesAdmin)
admin.site.register(Garage, GarageAdmin)
