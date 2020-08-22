from django.urls import path
from garage.views import GarageView, GarageDetailsView

app_name = "directory"

urlpatterns = [
    path('',            GarageView.as_view()),
    path('<int:pk>',    GarageDetailsView.as_view()),
]
