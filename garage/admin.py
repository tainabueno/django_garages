from django.contrib import admin
from garage.models import Vehicle, Garage

class VehiclesAdmin(admin.ModelAdmin):
    pass


class GarageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vehicle, VehiclesAdmin)
admin.site.register(Garage, GarageAdmin)
