from lib2to3.fixes.fix_input import context

from django.contrib.auth import get_user_model, login
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView, DeleteView

from Petstagram.accounts.forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm
from Petstagram.accounts.models import Profile
from Petstagram.photos.models import Photo

UserModel = get_user_model()


# Create your views here.
class AppUserRegisterView(views.CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = "accounts/register-page.html"
    success_url = reverse_lazy("home-page")

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #
    #     login(self.request, self.object)
    #     return response

class AppUserLoginView(auth_views.LoginView):
    form_class = AppUserLoginForm
    template_name = "accounts/login-page.html"

    def form_valid(self, form):
        super().form_valid(form)
        profile_instance, _ = Profile.objects.get_or_create(user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())

class AppUserLogoutView(auth_views.LogoutView):
    pass
class AppUserDetailView(views.DetailView):
    model = UserModel
    template_name = "accounts/profile-details-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_likes_count"] = sum(p.like_set.count() for p in self.object.photo_set.all())

        context["user_photos"] = (
            Photo.objects.filter(user_id=self.object.pk).
            order_by("-date_of_publication")
        )

        return context

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = "accounts/profile-edit-page.html"

    # def get_object(self, queryset=None):
    #     return self.request.user.profile

    def get_success_url(self, queryset=None):
        return reverse_lazy(
            "profile-details-page",
            kwargs={"pk": self.object.pk},
        )
class AppUserDeleteView(DeleteView):
    model = UserModel
    template_name = "accounts/profile-delete-page.html"
    success_url = reverse_lazy("home-page")

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())


