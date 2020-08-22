from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/garage/', include('garage.urls')),
    path('api/users/',  include('directory.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token)
]
