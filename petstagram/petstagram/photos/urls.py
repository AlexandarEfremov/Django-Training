from django.urls import path, include

from . import views

urlpatterns = [
    path('add/', views.photo_add_page, name="photo-add-page"),
    path('<int:pk>/', include([
        path('', views.photo_details_page, name="photo-details-page"),
        path('edit/', views.photo_edit_page, name="photo-edit-page")
    ]))
]