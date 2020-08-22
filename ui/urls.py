from django.urls import path
from ui import views

urlpatterns = [
    path('',                      views.GarageList.as_view(),      name='garage-list'),
    path('garage/<int:pk>/',      views.GarageUpdate.as_view(),    name='garage-update'),
    path('user/',                 views.UserCreate.as_view(),      name='user-add'),
    path('user/<int:pk>/',        views.UserUpdate.as_view(),      name='user-update'),
    path('vehicle/',              views.VehicleCreate.as_view(),   name='vehicle_add'),
    path('vehicle/<int:pk>/',     views.VehicleUpdate.as_view(),   name='vehicle-update'),
]
