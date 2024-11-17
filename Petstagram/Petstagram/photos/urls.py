from django.urls import path, include

from . import views
from .views import PhotoAddPage

urlpatterns = [
    path('add/', PhotoAddPage.as_view(), name="photo-add-page"),
    path('<int:pk>/', include([
        path('', views.photo_details_page, name='photo-details'),
        path('edit/', views.photo_edit_page, name='photo-edit-page'),
        path('delete/', views.photo_delete_page, name='photo-delete'),
    ])),
]