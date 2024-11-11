from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render
from django.views.generic import TemplateView

from Petstagram.accounts.forms import AppUserCreationForm

UserModel = get_user_model()


# Create your views here.
class AppUserRegisterView(views.CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = "accounts/register-page.html"
    success_url = reverse_lazy("login")

class LoginView(TemplateView):
    template_name = "accounts/login-page.html"

class ProfileDetailsPage(TemplateView):
    template_name = "accounts/profile-details-page.html"

class ProfileEditPage(TemplateView):
    template_name = "accounts/profile-edit-page.html"

class ProfileDeletePage(TemplateView):
    template_name = "accounts/profile-delete-page.html"

