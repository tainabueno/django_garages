from django.db import models, transaction
from django.contrib.auth.models import AbstractUser
from garage.models import Garage

class User(AbstractUser):

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    garage = models.OneToOneField(Garage, related_name='owner', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.garage=Garage.objects.create(phone=self.phone, email=self.email)
        super(User, self).save()
