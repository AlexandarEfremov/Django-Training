from django.urls import path

from world_of_speed.profiles.views import ProfileCreateView, ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='profile_create'),
    path('details/', ProfileDetailsView.as_view(), name='profile_details'),
    path('edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('delete/', ProfileDeleteView.as_view(), name='profile_delete')
]