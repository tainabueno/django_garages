from rest_framework.serializers import ModelSerializer
from directory.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')
