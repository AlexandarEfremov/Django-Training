from django.urls import path

from . import views

urlpatterns = [
    path("january", views.index) # if a requets reaches january then execute the views.index view
]