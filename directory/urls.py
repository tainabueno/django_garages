from django.urls import path
from directory.views import UserView, SingleUserView

app_name = 'users'

urlpatterns = [
    path('',            UserView.as_view()),
    path('<int:pk>',    SingleUserView.as_view()),
]
