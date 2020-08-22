from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from garage.models import Garage, Vehicle
from directory.models import User


class GarageForm(forms.ModelForm):
    vehicles = forms.ModelMultipleChoiceField(queryset=Vehicle.objects.all())

    class Meta:
        model = Garage
        exclude = ['is_active', 'phone', 'email']

    def __init__(self, *args, **kwargs):
        super(GarageForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['vehicles'].initial = self.instance.vehicles.all()

    def save(self, *args, **kwargs):
        instance = super(GarageForm, self).save(commit=False)
        self.fields['vehicles'].initial.update(garage=None)
        self.cleaned_data['vehicles'].update(garage=instance)
        return instance


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "name", "email", "phone")


class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "name", "email", "phone")
        exclude = ("password",)
