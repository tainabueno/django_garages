from rest_framework.serializers import ModelSerializer, StringRelatedField
from garage.models import Garage


class GarageSerializer(ModelSerializer):

    class Meta:
        model = Garage
        fields = ('is_active', 'owner')


class GarageVehiclesSerializer(ModelSerializer):
    vehicles = StringRelatedField(many=True)

    class Meta:
        model = Garage
        fields = ('is_active', 'vehicles', 'owner')
