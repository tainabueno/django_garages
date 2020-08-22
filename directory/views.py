from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from directory.models import User
from directory.serializers import UserSerializer


# Create your views here.
class UserView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.get_queryset().order_by('id')
    serializer_class = UserSerializer


class SingleUserView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.get_queryset().order_by('id')
    serializer_class = UserSerializer
