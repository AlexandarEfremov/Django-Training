from django.urls import path, include

from world_of_speed.cars.views import CreateCarView, CatalogueView, CarDetailsView, CarEditView, \
    CarDeleteView

urlpatterns = [
    path('catalogue/', CatalogueView.as_view(), name='car_catalogue'),
    path('create/', CreateCarView.as_view(), name='car_create'),
    path('<int:pk>', include([
        path('details/', CarDetailsView.as_view(), name='car_details'),
        path('edit/', CarEditView.as_view(), name='car_edit'),
        path('delete/', CarDeleteView.as_view(), name='car_delete'),
    ]))
]
