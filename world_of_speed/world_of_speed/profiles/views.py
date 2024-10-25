from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, DeleteView

from world_of_speed.profiles.forms import ProfileCreateForm, ProfileDetailsForm
from world_of_speed.profiles.models import Profile
from world_of_speed.web.views import get_profile


class BaseView(TemplateView):
    pass


class NavBarMixin(BaseView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context


class ProfileCreateView(CreateView): #CreateView doesn't have obj and can't inherit Mixin
    model = Profile
    form_class = ProfileCreateForm
    template_name = "profiles/profile-create.html"
    success_url = reverse_lazy("car_catalogue")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = "profiles/profile-details.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return get_profile()


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileDetailsForm
    template_name = "profiles/profile-edit.html"
    success_url = reverse_lazy("profile_details")

    def get_object(self, queryset=None):
        return get_profile()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = "profiles/profile-delete.html"
    context_object_name = "profile"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()



