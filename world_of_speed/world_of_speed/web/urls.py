from django.urls import path

from world_of_speed.web import views

urlpatterns = [
    path('', views.index, name='index')
]