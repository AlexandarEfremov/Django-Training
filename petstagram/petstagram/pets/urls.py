from django.urls import path, include

from . import views

urlpatterns = [
    path('add/', views.AddPetView.as_view(), name="pet-add-page"),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.PetDetailsView.as_view(), name="pet-details-page"),
        path('edit/', views.EditPetView, name="pet-edit-page"),
        path('delete/', views.DeletePetView.as_view(), name="pet-delete-page")
    ])),
]