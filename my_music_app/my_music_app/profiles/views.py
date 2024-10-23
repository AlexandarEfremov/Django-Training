from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from my_music_app.profiles.models import Profile
from my_music_app.web.views import get_profile


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = "profile/profile-details.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return get_profile()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = "profile/profile-delete.html"
    context_object_name = "profile"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()





