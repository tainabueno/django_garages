from django.urls import path
from directory.views import (
    UserView,
    SingleUserView,
    UserWithVehiclesView,
    UserWithoutVehiclesView )

app_name = 'users'

urlpatterns = [
    path('',                  UserView.as_view()),
    path('<int:pk>',          SingleUserView.as_view()),
    path('motorized/',        UserWithVehiclesView.as_view()),
    path('non_motorized/',    UserWithoutVehiclesView.as_view()),
]
