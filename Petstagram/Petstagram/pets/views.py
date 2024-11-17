from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Pet
from .forms import PetForm, PetDeleteForm
from ..common.forms import CommentForm


class AddPetView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-add-page.html'

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile-details-page', kwargs={"pk": self.request.user.pk})

class PetDetailsView(DetailView):
    model = Pet
    template_name = "pets/pet-details-page.html"
    context_object_name = "pet"
    slug_url_kwarg = "pet_slug" #this basically tells django that the dynamic value name is pet_slug, as by default
    #it's slug, which might break the code

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_photos"] = self.object.photo_set.all()
        context["comment_form"] = CommentForm()
        return context

class EditPetView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = "pets/pet-edit-page.html"
    slug_url_kwarg = "pet_slug"
    context_object_name = "pet"

    def get_success_url(self):
        return reverse_lazy("pet-details-page", kwargs={
            "username": self.kwargs["username"],
            "pet_slug": self.kwargs["pet_slug"]
        })

class DeletePetView(DeleteView):
    model = Pet
    template_name = "pets/pet-delete-page.html"
    context_object_name = "pet"
    success_url = reverse_lazy("profile-details-page", kwargs={"pk": 1})

    def get_object(self, queryset=None):
        return Pet.objects.get(slug=self.kwargs["pet_slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PetDeleteForm(initial=self.object.__dict__)

    def delete(self, request, *args, **kwargs):
        pet = self.get_object()
        pet.delete()
        return redirect(self.success_url)