from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from garage.models import Garage
from garage.serializers import GarageSerializer, GarageVehiclesSerializer
from garage.permissions import IsOwnerOrReadOnly

class GarageView(ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Garage.objects.get_queryset().order_by('id')
    serializer_class = GarageSerializer


class GarageDetailsView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Garage.objects.get_queryset().order_by('id')
    serializer_class = GarageVehiclesSerializer
