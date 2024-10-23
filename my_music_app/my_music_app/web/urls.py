from django.urls import path

from my_music_app.web import views

urlpatterns = [
    path("create-profile/", views.create_profile, name="create_profile"),
    path('', views.index, name='index'),

]

