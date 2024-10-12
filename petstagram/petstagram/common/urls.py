from django.urls import path

from petstagram.petstagram.common import views

urlpatterns = (
    path('', views.home_page, name="home_page")
)