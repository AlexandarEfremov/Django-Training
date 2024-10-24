from django.urls import path

from fruitipedia.profiles import views
from fruitipedia.profiles.views import CreateProfileView, DetailsProfileView, EditProfileView

urlpatterns = [
    path('create/', CreateProfileView.as_view(), name='profile_create'),
    path('details/', DetailsProfileView.as_view(), name='profile_details'),
    path('edit/', EditProfileView.as_view(), name='profile_edit'),
    path('delete/', views.DeleteProfileView.as_view(), name='profile_delete'),
]