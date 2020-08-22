from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from garage.models import Garage, Vehicle
from garage.forms import GarageForm, UserRegisterForm, UserUpdateForm
from directory.models import User
from django.forms.models import modelform_factory


class GarageList(ListView):
    model = Garage


class GarageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'garage/garage_form.html'
    model = Garage
    form_class = GarageForm
    success_url = reverse_lazy('garage-list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user != self.get_object().owner:
            return HttpResponseRedirect("/")
        return super().get(request, *args, **kwargs)


class UserCreate(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('garage-list')


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('garage-list')


class VehicleCreate(LoginRequiredMixin, CreateView):
    model = Vehicle
    fields = '__all__'
    success_url = reverse_lazy('garage-list')


class VehicleUpdate(LoginRequiredMixin, UpdateView):
    model = Vehicle
    fields = '__all__'
    success_url = reverse_lazy('garage-list')
