from django.db import models, transaction
from garage.models import Garage
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    garage = models.OneToOneField(Garage, related_name='owner', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.garage=Garage.objects.create()
        super(User, self).save()
