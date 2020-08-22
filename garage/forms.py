from django import forms
from django.db import models

from garage.models import Garage, Vehicle

class GarageForm(forms.ModelForm):

    class Meta:
        model = Garage
        exclude = ()

    vehicles = forms.ModelMultipleChoiceField(queryset=Vehicle.objects.all())

    def __init__(self, *args, **kwargs):
        super(GarageForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['vehicles'].initial = self.instance.vehicles.all()

    def save(self, *args, **kwargs):
        # FIXME: 'commit' argument is not handled
        # TODO: Wrap reassignments into transaction
        # NOTE: Previously assigned Foos are silently reset
        instance = super(GarageForm, self).save(commit=False)
        self.fields['vehicles'].initial.update(garage=None)
        self.cleaned_data['vehicles'].update(garage=instance)
        return instance