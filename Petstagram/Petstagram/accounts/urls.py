from django.urls import path, include

from . import views
from .views import ProfileDetailsPage, ProfileEditPage, ProfileDeletePage, AppUserRegisterView, AppUserLoginView

urlpatterns = [
    path('register/', AppUserRegisterView.as_view(), name="register"),
    path('login/', AppUserLoginView.as_view(), name="login"),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsPage.as_view(), name="profile-details-page"),
        path('edit/', ProfileEditPage.as_view(), name="profile-edit-page"),
        path('delete/', ProfileDeletePage.as_view(), name="profile-delete-page")
    ])),
]