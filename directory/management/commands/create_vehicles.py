import csv

from django.core.management.base import BaseCommand
from garage.models import Vehicle


class Command(BaseCommand):

    def handle(self, *args, **options):

        with open('vehicles.csv') as csvfile:
            list_of_vehicles = csv.reader(csvfile, delimiter=',')
            next(list_of_vehicles)

            for row in list_of_vehicles:
                Vehicle.objects.create(model=row[0],
                                       color=row[1],
                                       brand=row[2],
                                       body=row[3],
                                       year=row[4]).save()
