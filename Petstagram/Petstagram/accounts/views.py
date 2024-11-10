from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class RegisterView(TemplateView):
    template_name = "accounts/register-page.html"

class LoginView(TemplateView):
    template_name = "accounts/login-page.html"

class ProfileDetailsPage(TemplateView):
    template_name = "accounts/profile-details-page.html"

class ProfileEditPage(TemplateView):
    template_name = "accounts/profile-edit-page.html"

class ProfileDeletePage(TemplateView):
    template_name = "accounts/profile-delete-page.html"

