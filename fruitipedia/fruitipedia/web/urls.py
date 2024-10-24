from django.urls import path

from fruitipedia.web import views


urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name='dashboard')
]