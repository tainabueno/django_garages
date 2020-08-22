import json

from django.db import models
from directory import models as dm

class Garage(models.Model):

    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "Garage Number %s, Owner: %s" % (self.id, self.owner)

    def list_of_vehicles(self):
        return json.loads(Vehicle.objects.filter(garage=self))


class Vehicle(models.Model):

    VW = "vw"
    FIAT = "fiat"
    GM = "gm"
    FORD = "ford"
    BRANDS = [
        (VW,   "VW"),
        (FIAT, "Fiat"),
        (GM,   "GM"),
        (FORD, "Ford"),
    ]

    CAR = "car"
    MOTORCYCLE = "motorcycle"
    BODIES = [
        (CAR,   "Car"),
        (MOTORCYCLE, "Motorcycle"),
    ]

    BLUE = "blue"
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"
    BLACK = "black"
    WHITE = "white"


    COLORS = [
        (RED,   "Red"),
        (BLUE, "Blue"),
        (GREEN,   "Green"),
        (YELLOW, "Yellow"),
        (BLACK,   "Black"),
        (WHITE, "White"),
    ]

    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255, choices=COLORS)
    brand = models.CharField(max_length=255, choices=BRANDS)
    body = models.CharField(max_length=255, choices=BODIES)
    year = models.IntegerField()
    garage = models.ForeignKey(Garage, related_name='vehicles', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.model}, {self.year}, {self.color}, {self.body}"


    def config(self):
        if self.body == Vehicle.MOTORCYCLE:
            return self.model
        return (self.color, self.year)