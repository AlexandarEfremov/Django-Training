from django.urls import path

from . import views

urlpatterns = [
    # path("january", views.january), # if a requets reaches january then execute the views.index view
    # path("february", views.february)
     #this is a placeholder, meaning django will accept any month
    path("<int:month>", views.integer_months), #this converts the string into an int
    path("<month>", views.monthly_challenge)
]