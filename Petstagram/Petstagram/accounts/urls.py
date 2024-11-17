from django.urls import path, include

from . import views
from .views import ProfileDetailsPage, ProfileDeletePage, AppUserRegisterView, AppUserLoginView, \
    AppUserLogoutView, ProfileEditView

urlpatterns = [
    path('login/', AppUserLoginView.as_view(), name="login"),
    path('register/', AppUserRegisterView.as_view(), name="register"),
    path('logout/', AppUserLogoutView.as_view(), name="logout"),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsPage.as_view(), name="profile-details-page"),
        path('edit/', ProfileEditView.as_view(), name="profile-edit-page"),
        path('delete/', ProfileDeletePage.as_view(), name="profile-delete-page")
    ])),
]