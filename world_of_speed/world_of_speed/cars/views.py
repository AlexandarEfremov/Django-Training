from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from world_of_speed.cars.forms import CreateCarForm
from world_of_speed.cars.models import Car
from world_of_speed.web.views import get_profile


class CreateCarView(CreateView):
    model = Car
    form_class = CreateCarForm
    template_name = "cars/car-create.html"
    success_url = reverse_lazy("car_catalogue")

    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context

class CatalogueView(ListView):
    model = Car
    template_name = "cars/catalogue.html"
    context_object_name = "cars"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context


class CarDetailsView(DetailView):
    model = Car
    template_name = "cars/car-details.html"
    context_object_name = "car"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context


class CarEditView(UpdateView):
    model = Car
    form_class = CreateCarForm
    template_name = "cars/car-edit.html"
    success_url = reverse_lazy("car_catalogue")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context

class CarDeleteView(DeleteView):
    model = Car
    template_name = "cars/car-delete.html"
    context_object_name = "car"
    success_url = reverse_lazy("car_catalogue")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.get_object()
        form = CreateCarForm(instance=album)
        for field in form.fields.values():
            field.disabled = True
        context['form'] = form
        return context