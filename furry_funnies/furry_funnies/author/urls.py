from django.urls import path

from furry_funnies.author import views
from furry_funnies.author.views import AuthorCreateView, AuthorDetailsView, AuthorEditView, AuthorDeleteView

urlpatterns=[
    path('create/', AuthorCreateView.as_view(), name='author_create'),
    path('details/', AuthorDetailsView.as_view(), name='author_details'),
    path('edit/', AuthorEditView.as_view(), name='author_edit'),
    path('delete/', AuthorDeleteView.as_view(), name='author_delete')
]
