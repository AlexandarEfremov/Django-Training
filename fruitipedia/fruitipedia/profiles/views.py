from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from fruitipedia.profiles.forms import CreateProfileForm, EditProfileForm
from fruitipedia.profiles.models import Profile
from fruitipedia.web.views import get_profile


# Create your views here.

class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = "profiles/create-profile.html"
    success_url = reverse_lazy("dashboard")


class DetailsProfileView(DetailView):
    model = Profile
    template_name = "profiles/details-profile.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return get_profile()


class EditProfileView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = "profiles/edit-profile.html"
    success_url = reverse_lazy("profile_details")

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(DeleteView):
    model = Profile
    template_name = "profiles/delete-profile.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()