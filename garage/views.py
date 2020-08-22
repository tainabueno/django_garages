from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from garage.models import Garage
from garage.serializers import GarageSerializer, GarageVehiclesSerializer
from garage.permissions import OnlyOwners

class GarageView(ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Garage.objects.filter(is_active=True).order_by('id')
    serializer_class = GarageSerializer


class GarageDetailsView(RetrieveUpdateDestroyAPIView):
    permission_classes = (OnlyOwners, )
    queryset = Garage.objects.get_queryset().order_by('id')
    serializer_class = GarageVehiclesSerializer
