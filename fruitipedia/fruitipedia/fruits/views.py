from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, TemplateView

from fruitipedia.fruits.forms import CreateFruitForm, EditFruitForm
from fruitipedia.fruits.models import Fruit
from fruitipedia.web.views import get_profile


class BaseView(TemplateView):
    pass


class NavBarMixin(BaseView):
    def get_context_data(self, **kwargs):
        context = kwargs  # Use the provided kwargs directly as context
        profile = get_profile()  # Assuming get_profile() is defined elsewhere
        context['profile'] = profile
        return context

class CreateFruitView(CreateView, NavBarMixin):
    model = Fruit
    form_class = CreateFruitForm
    template_name = "fruits/create-fruit.html"
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)



class DetailsFruitView(DetailView, NavBarMixin):
    model = Fruit
    template_name = "fruits/details-fruit.html"
    context_object_name = "fruit"



class EditFruitView(UpdateView, NavBarMixin):
    model = Fruit
    form_class = EditFruitForm
    template_name = "fruits/edit-fruit.html"
    success_url = reverse_lazy('dashboard')


class DeleteFruitView(DeleteView, NavBarMixin):
    model = Fruit
    template_name = "fruits/delete-fruit.html"
    success_url = reverse_lazy('dashboard')
    context_object_name = "fruit"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fruit = self.get_object()
        form = EditFruitForm(instance=fruit)
        for field in form.fields.values():
            field.disabled = True

        context['form'] = form
        return context