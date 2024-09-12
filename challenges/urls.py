from django.urls import path

from . import views

urlpatterns = [
    # path("january", views.january), # if a requets reaches january then execute the views.index view
    # path("february", views.february)
    path("<month>", views.monthly_challenge) #this is a placeholder, meaning django will accept any month
]