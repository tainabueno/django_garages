from django.db import models, transaction
from garage.models import Garage
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return "%s, %s" % (self.name, self.email)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.garage=Garage.objects.create()
        super(User, self).save()
