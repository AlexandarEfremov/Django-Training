from django.urls import path, include

from . import views

urlpatterns = [
    # path('register/', views.register, name="register"),
    # path('login/', views.login, name="login"),
    # path('profile/<int:pk>/', include([
    #     path('', views.profile_details_page, name="profile-details-page"),
    #     path('edit/', views.profile_edit_page, name="profile-edit-page"),
    #     path('delete/', views.profile_delete_page, name="profile-delete-page")
    # ])),
]