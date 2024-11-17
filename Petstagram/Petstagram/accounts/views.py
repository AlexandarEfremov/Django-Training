from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render
from django.views.generic import TemplateView

from Petstagram.accounts.forms import AppUserCreationForm, AppUserLoginForm
from Petstagram.accounts.models import Profile

UserModel = get_user_model()


# Create your views here.
class AppUserRegisterView(views.CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = "accounts/register-page.html"
    success_url = reverse_lazy("login")

class AppUserLoginView(auth_views.LoginView):
    form_class = AppUserLoginForm
    template_name = "accounts/login-page.html"

    def form_valid(self, form):
        super().form_valid(form)
        profile_instance, _ = Profile.objects.get_or_create(user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())

class AppUserLogoutView(auth_views.LogoutView):
    pass
class ProfileDetailsPage(TemplateView):
    template_name = "accounts/profile-details-page.html"

class ProfileEditPage(TemplateView):
    template_name = "accounts/profile-edit-page.html"

class ProfileDeletePage(TemplateView):
    template_name = "accounts/profile-delete-page.html"

