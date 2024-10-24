from django.urls import path
from fruitipedia.fruits.views import CreateFruitView, DetailsFruitView, EditFruitView, DeleteFruitView

urlpatterns =[
    path('create/', CreateFruitView.as_view(), name='create_fruit'),
    path('<int:pk>/details/', DetailsFruitView.as_view(), name='fruit_details'),
    path('<int:pk>/edit/', EditFruitView.as_view(), name='fruit_edit'),
    path('<int:pk>/delete/', DeleteFruitView.as_view(), name='fruit_delete'),
]