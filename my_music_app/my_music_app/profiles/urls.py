from django.urls import path

from my_music_app.profiles.views import ProfileDetailsView, ProfileDeleteView
from my_music_app.web.views import index, create_profile

urlpatterns = [
    path('create-profile/', create_profile, name='create_profile'),
    path('details/', ProfileDetailsView.as_view(), name='profile_details'),
    path('delete/', ProfileDeleteView.as_view(), name='profile_delete')
]